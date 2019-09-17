import redis
import json
import datetime
from simplejson.encoder import JSONEncoder

class MyjsonDecode(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, datetime.date):
            return o.strftime('%Y-%m-%d')
        else:
            return JSONEncoder.default(self, o)


def encodev(o):
    return json.dumps(o, cls=MyjsonDecode, encoding="utf-8")


def decodev(o):
    if not isinstance(o, bytes):
        return o
    data = json.loads(o)
    return data

Pool = redis.ConnectionPool(host="152.136.169.216", port="6379", password="mima@tbkt123", db=1)


class Conn(object):
    def __init__(self):
        if not hasattr(self, "conn"):
            self.conn = redis.Redis(connection_pool=Pool)

    def set(self, key, value, ctime=None):
        value = encodev(value)
        if ctime:
            self.conn.setex(key, value, ctime)
        else:
            self.conn.set(key, value)

    def get(self, key):
        value = self.conn.get(key)
        if value:
            return decodev(value)
        return None

    def delete(self, key):
        self.conn.delete(key)

rd = Conn()
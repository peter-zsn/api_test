import pymysql
from DBUtils.PooledDB import PooledDB
import asyncio
import time
import threading

class DB(object):
    def __init__(self):
        self.db_pools = {}


    def add_pool(self, db=None):
        pool = PooledDB(
            creator=pymysql,
            host="116.255.220.101",
            port=3369,
            db=db,
            user="zhangshuainan",
            passwd="shuainan@tbkt2017!",
            charset='utf8',
            ping=0,
            maxconnections=8,
        )
        if db not in self.db_pools.keys():
            self.db_pools[db] = pool

    def __getattr__(self, item):
        pool = self.db_pools.get(item)
        if pool:
            return Connection(pool)


class Connection(object):
    def __init__(self, pool):
        if not hasattr(self, "_pool"):
            self._pool = pool
        self.conn = self.get_conn(timeout=2)
        self.cursor = self.conn.cursor()

    def get_conn(self, timeout=1):
        if not hasattr(self, "_conn"):
            while 1:
                try:
                    _conn = self._pool.connection()
                    return _conn
                except Exception as e:
                    time.sleep(timeout)
                    return self.get_conn()

    def fetchall(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def fetchone(self, sql):
        self.execute(sql)
        return self.cursor.fetchone()

    def fetchall_dict(self, sql):
        self.cursor.execute(sql)
        fields = [r[0] for r in self.cursor.description]
        rows = self.cursor.fetchall()
        return [dict(zip(fields, row)) for row in rows]

    def fetchone_dict(self, sql):
        self.cursor.execute(sql)
        fields = [r[0] for r in self.cursor.description]
        row = self.cursor.fetchone()
        return dict(zip(fields, row))

    def execute(self, sql):
        self.cursor.execute(sql)
        return self.cursor.rowcount, self.cursor.lastrowid

    def __del__(self):
        self.cursor.close()
        self.conn.close()

db = DB()
db.add_pool("tbkt_base")

async def do_sql(sql, x):
    res = db.tbkt_base.fetchall(sql)
    print(x)

def do_sql_test(sql, x):
    res = db.tbkt_base.fetchall_dict(sql)
    print(res)


if __name__ == "__main__":
    sql = "SELECT id, phone FROM auth_account LIMIT 10;"
    do_sql_test(sql, 1)
    # print(time.time(), 111111111111)
    # loop = asyncio.get_event_loop()
    # tasks = []
    # for i in range(1, 100):
    #     work = do_sql(sql, i)
    #     tasks.append(asyncio.ensure_future(work))
    #
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()
    # print(time.time(), 222222222222)
    # print(time.time(), 111111111111111)
    # works = []
    # for i in range(1, 1000):
    #     t = threading.Thread(target=do_sql_test, args=(sql, i))
    #     works.append(t)
    #
    # for t in works:
    #     t.start()
    # for t in works:
    #     t.join()
    # print(time.time(), 3333333333333333)
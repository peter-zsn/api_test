# coding: utf-8
import json as simplejson
from json.encoder import JSONEncoder
import datetime
from django.http import HttpResponse


class XJSONEncoder(JSONEncoder):
    """
    JSON扩展: 支持datetime和date类型
    """
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, datetime.date):
            return o.strftime('%Y-%m-%d')
        else:
            return JSONEncoder.default(self, o)
        
def json_response(data):
    r = HttpResponse(simplejson.dumps(data, cls=XJSONEncoder))
    r['Content-Type'] = 'application/json'
    return r


def ajax_ok(data=None, message=""):
    res = dict(data=data, message=message, response='ok')
    return json_response(res)


def ajax_fail(data=None, message=""):
    res = dict(data=data, message=message, response='fail')
    return json_response(res)
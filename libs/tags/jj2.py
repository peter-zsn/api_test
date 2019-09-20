import time
import datetime
from jinja2 import Environment
from jinja2.runtime import Undefined


def finalize(o):
    "把None换成空"
    return '' if o is None else o

class MyUndefined(object):
    "把未定义变量处理为None"

    def __init__(self, *args, **kwargs):
        pass

    def __getattr__(self, name):
        if name[:2] == '__':
            raise AttributeError(name)
        return None

    def __str__(self):
        return u''

    def __len__(self):
        return 0

    def __iter__(self):
        if 0:
            yield None

    def __nonzero__(self):
        return False

    __bool__ = __nonzero__

    def __repr__(self):
        return ''

def do_date(date, format):
    """时间格式化, 支持整数时间戳
    ~ 用法：{{xxx|date('%Y-%m-%d %H:%M:%S')}}
    """
    if not date:
        return u''
    if isinstance(date, int):
        t = time.localtime(date)
        date = datetime.datetime(*t[:6])
    s = date.strftime(format)
    return s

filters = {
    'date': do_date,
}

class Env(Environment):
    def __init__(self, *args, **kw):
        kw['extensions'] = ('jinja2.ext.with_',)  # 启用with语句
        Environment.__init__(self, *args, **kw)
        # 把未定义变量和None处理为空字符串
        self.finalize = finalize
        self.undefined = MyUndefined
        self.filters.update(filters)

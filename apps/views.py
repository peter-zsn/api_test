from libs.utils.com_redis import rd
from libs.utils import ajax

def login(request):
    username = request.QUERY.get("username")
    password = request.QUERY.get("password")
    if not username or not password:
        return ajax.ajax_fail(message="请输入账号密码")
    rel_pwd = rd.get(username)
    if rel_pwd == password:
        return ajax.ajax_ok(message="登陆成功")
    else:
        return ajax.ajax_fail(message="账号密码错误")


def register(request):
    username = request.QUERY.get("username")
    password = request.QUERY.get("password")
    rd.set(username, password)
    return ajax.ajax_ok(message="注册成功")
"""coding: utf-8"""
from django.http import HttpResponseRedirect

from libs.utils.com_redis import rd
from libs.utils import ajax
from com.common import add_login

def login(request):
    if request.method == "GET":
        data = {
            "message": "欢迎"
        }
        return ajax.rendet_template(request, "login.html", data)

    username = request.QUERY.get("username")
    password = request.QUERY.get("password")
    if not username or not password:
        return ajax.ajax_fail(request, message="请输入账号密码")
    rel_pwd = rd.get(username)
    if rel_pwd == password:
        resp = ajax.ajax_ok(request, message="登陆成功")
        add_login(resp, username)
        return resp
    else:
        return ajax.ajax_fail(request, message="账号密码错误")


def logout(request):
    rep = HttpResponseRedirect("/my/login")
    rep.delete_cookie("username")
    return rep

def register(request):
    if request.method == "GET":
        return ajax.rendet_template(request, "register.html", {})

    username = request.QUERY.get("username")
    password = request.QUERY.get("password")
    if not username or not password:
        return ajax.ajax_fail(request, message="请输入账号密码!")
    passed = rd.get(username)
    if passed:
        return ajax.ajax_fail(request, message="您已经注册过了，请返回首页点击找回密码进行使用!")
    rd.set(username, password)
    return ajax.ajax_ok(request, message="注册成功!")


def find_pass(request):
    username = request.QUERY.get("username")
    if not username:
        return ajax.ajax_fail(request, message="请输入账号!")
    passwd = rd.get(username)
    if not passwd:
        return ajax.ajax_fail(request, message="账号不存在!")
    return ajax.ajax_ok(request, {"pass": passwd})


def index(request):
    return ajax.rendet_template(request, "index.html", {})

def change_pass(request):
    username = request.username
    old_pass = request.QUERY.get("old_pass")
    new_pass = request.QUERY.get("new_pass")
    passwd = rd.get(username)
    if passwd != old_pass:
        return ajax.ajax_fail(request, message="密码错误")
    rd.set(username, new_pass)
    return ajax.ajax_ok(request, {})

def welcome(request):
    return ajax.rendet_template(request, "welcome.html", {})
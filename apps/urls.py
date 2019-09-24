from django.conf.urls import url, include

from apps import views

urlpatterns = [
    url(r'^login$', views.login),              # 登陆接口
    url(r'^register$', views.register),        # 注册接口
    url(r'^find_pass$', views.find_pass),      # 注册接口
    url(r'^index$', views.index),              # 首页
    url(r'^change_pass$', views.change_pass),              # 修改密码
    url(r'^welcome$', views.welcome),              # 欢迎页面
    url(r'^logout$', views.logout),              # 退出
]
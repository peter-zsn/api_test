# coding: utf-8
from django.conf.urls import url, include

from apps.movies import views

urlpatterns = [
    url(r'^getList$', views.getList),              # 获取电影列表信息接口

]
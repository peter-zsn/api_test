from django.conf.urls import url, include

from apps import views

urlpatterns = [
    url(r'^login$', views.login),            # 登陆接口
    url(r'^register$', views.register)       # 注册接口
]
#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#@File    :   urls.py
#@Time    :   2020/09/23 14:17:24
#@Author  :   Mr.W
#@Email   :   476063646@qq.com

"""定义learning_logs的URL模式"""

from django.conf.urls import url
from . import views

app_name='learning_logs'

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有主题
    url(r'^topics/$', views.topics, name='topics'),

    # 特定主题的详细页面 
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # 用于添加新主题的网页 
    url(r'^new_topic/$', views.new_topic, name='new_topic'),    
]

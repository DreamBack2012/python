#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#@File    :   forms.py
#@Time    :   2020/09/24 09:13:02
#@Author  :   Mr.W
#@Email   :   476063646@qq.com

from django import forms 
from .models import Topic

class TopicForm(forms.ModelForm): 
    class Meta: 
        model = Topic 
        fields = ['text'] 
        labels = {'text': ''}

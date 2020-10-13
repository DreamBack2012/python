#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#@File    :   help.py
#@Time    :   2020/09/09 18:05:15
#@Author  :   Mr.W
#@Email   :   476063646@qq.com

import sys, os
from PyQt5.QtWidgets import QWidget

# 使用dir()函数打印QWidget对象的属性和函数
# print(dir(QWidget))

# help()用来查看类的说明文档
# print(help(QWidget))

filename = os.path.join(sys.path[0], "QWidget.txt")
out = sys.stdout
sys.stdout = open(filename ,'w')
help(QWidget)
sys.stdout.close()
sys.stdout = out

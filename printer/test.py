#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#@File    :   test.py
#@Time    :   2020/08/25 11:49:56
#@Author  :   Mr.W
#@Email   :   476063646@qq.com

import sys, getopt
from printer import Printer
from toshiba import Toshiba

# 打印机ip地址
ip = '192.168.10.17'

# 获取打印机类型
printer_type = 'toshiba'

# 根据打印机类型创建打印机对象
if printer_type == 'toshiba':
    printer = Toshiba(ip)
else:
    printer = printer(ip)

# 根据命令行处理指令，如果未传入指令，则使用默认指令
cmd = 'init'
if len(sys.argv) > 1:
    cmd = sys.argv[1]

if cmd == 'init':
    printer.init()
elif cmd == 'unlock':
    printer.unlock()
elif cmd == 'lock':
    printer.lock()
elif cmd == 'info':
    printer.info()
elif cmd == 'paper':
    printer.paper()            
elif cmd == 'data':
    printer.data()
else:
    print("unsupported cmd:", cmd)

#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#@File    :   toshiba.py
#@Time    :   2020/08/25 15:14:18
#@Author  :   Mr.W
#@Email   :   476063646@qq.com


import sys, getopt, os
import requests
from printer import Printer

class Toshiba(Printer):
    # 东芝打印机

    def __init__(self, ip):
        # 初始化父类的属性
        super().__init__(ip)
        self.cookies = ''

    def login(self):
        print("login")


    def init(self):
        """打印机初始化操作"""
        self.login()
        

    def unlock(self):
        self.login()

    def data(self):
        # 数据采集
        self.counter()

    def counter(self):
        # 计数器
        cmd_header = 'snmpwalk -v 2c -c public '
        mib = 'iso.3.6.1.4.1.1129.2.3.50.1.3.21.6.1'
        cmd = cmd_header + self.ip + " " + mib
        result = os.popen(cmd).read()
        print(result)

if __name__ == '__main__':
    printer = Toshiba("192.168.10.17")
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

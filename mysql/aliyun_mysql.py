#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#@File    :   aliyun_mysql.py
#@Time    :   2020/09/03 09:33:21
#@Author  :   Mr.W
#@Email   :   476063646@qq.com

import pymysql
from sshtunnel import SSHTunnelForwarder

class AliyunMysql():
    """阿里云mysql管理"""

    def __init__(self):
        # 初始化ssh通道参数
        self.ssh_host = "119.23.251.170"        # ssh服务器地址
        self.ssh_port = 12222                   # ssh端口
        # self.ssh_pkey = ""                    # ssh密钥
        self.ssh_user = "wm"                    # ssh用户名
        self.ssh_passwd = "XtyG0b1dvm_sHnxZ"    # ssh密码

        # 初始化数据库连接参数
        self.db_host = "rm-wz95m7bq58aixi4s0.mysql.rds.aliyuncs.com"    # 数据库地址
        self.db_port = 3306                                             # 数据库端口
        self.db_user = "root"                                           # 数据库用户名
        self.db_passwd = "w6m3BbTrr_t25QV2lfKr"                         # 数据库密码
        self.db_name = "zxy_person"                                     # 数据库名

    def connect(self):
        # 连接服务器
        self.server = SSHTunnelForwarder(
                (self.ssh_host, self.ssh_port),
                ssh_password=self.ssh_passwd,
                # ssh_pkey=self.ssh_pkey,
                ssh_username=self.ssh_user,
                remote_bind_address=(self.db_host, self.db_port)
        )
        self.server.start()

        self.connection = pymysql.connect(
            host='127.0.0.1',
            port=self.server.local_bind_port,
            user=self.db_user,
            passwd=self.db_passwd,
            db=self.db_name,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor)

        self.cursor = self.connection.cursor()

    def disconnect(self):
        # 断开连接
        self.cursor.close()
        self.connection.close()
        self.server.stop()

    def query(self, sql):
        # 通过sql查询数据
        try:
            print(sql)
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            # self.connection.commit()
        except:
            self.connection.rollback()
        return data

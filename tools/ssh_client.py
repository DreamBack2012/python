#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#@File    :   ssh_client.py
#@Time    :   2020/09/07 16:18:33
#@Author  :   Mr.W
#@Email   :   476063646@qq.com

import sys, logging
import paramiko

class SshClient():
    """
    ssh客户端，用于远程连接服务器
    可通过用户名或密钥进行登录
    执行传入的命令并返回执行结果
    """

    def __init__(self):
        # 初始化
        self.ssh_client = paramiko.SSHClient()

    def connect(self, host, port, username, password, pkey = ""):
        # 连接ssh服务器
        try:
            # 设置允许连接known_hosts文件中的主机（默认连接不在known_hosts文件中的主机会拒绝连接抛出SSHException）
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            if pkey != "":
                private_key = paramiko.RSAKey.from_private_key_file(pkey)
                self.ssh_client.connect(host, port=port, username=username, pkey=private_key)
            else:
                self.ssh_client.connect(host, port=port, username=username, password=password)
        except paramiko.AuthenticationException:
            logging.warning('username or password error')
            return 1
        except paramiko.ssh_exception.NoValidConnectionsError:
            logging.warning('connect time out')
            return 2            
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return 3
        return 0

    def exec_command(self, cmd):
        # 执行命令
        result = self.ssh_client.exec_command(cmd)
        # 获取命令结果
        out = result[1].read()
        err = result[2].read()
        result = out if out else err
        return result.decode()

    def disconnect(self):
        # 断开连接
        self.ssh_client.close()

if __name__ == "__main__":
    cmd = 'ls -l ~/'
    ssh = SshClient()
    if ssh.connect('192.168.10.31', 22, 'wm', 'abcd123') == 0:
        result = ssh.exec_command(cmd)
        print(result)
        ssh.disconnect()

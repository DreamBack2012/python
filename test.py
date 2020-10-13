import sys,logging
from paramiko.client import SSHClient, AutoAddPolicy
from paramiko import AuthenticationException
from paramiko.ssh_exception import NoValidConnectionsError
 
class SshClient():
    def __init__(self):
        self.ssh_client = SSHClient()
 
    def ssh_login(self, host_ip, username, password):
        try:
            # 设置允许连接known_hosts文件中的主机（默认连接不在known_hosts文件中的主机会拒绝连接抛出SSHException）
            self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())
            self.ssh_client.connect(host_ip, port=22, username=username, password=password)
        except AuthenticationException:
            logging.warning('username or password error')
            return 1001
        except NoValidConnectionsError:
            logging.warning('connect time out')
            return 1002
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return 1003
        return 1000
 
    def execute_some_command(self, command):
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        print(stdout.read().decode())
 
    def ssh_logout(self):
        self.ssh_client.close()
 
if __name__ == "__main__":
    command = "ls"       # 自己使用ssh时，命令怎么敲的command参数就怎么写
    ssh = SshClient()
    if ssh.ssh_login(host_ip="192.168.10.11", username="root", password="abcd123") == 1000:
        ssh.execute_some_command(command)
        ssh.ssh_logout()
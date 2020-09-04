
class Printer():
    """打印机基类"""

    def __init__(self, ip):
        # 初始化打印机IP地址
        self.ip = ip
        self.url = "http://" + ip + "/"
    
    def init(self):
        # 初始化操作，只有执行完这些操作，才能继续执行其它指令
        print("do init")

    def unlock(self):
        # 解锁指令，关闭面板控制
        print("do unlock")

    def lock(self):
        # 锁定指令，打开面板控制
        print("do lock")

    def info(self):
        # 获取打印机名称、序列号、版本信息
        print("get info")
    
    def paper(self):
        # 确定纸盒中是否有纸
        return True
    
    def data(self):
        # 获取打印机状态、纸盒、碳粉、鼓、计数器
        print("data")
#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#@File    :   qrcode.py
#@Time    :   2020/09/15 10:12:44
#@Author  :   Mr.W
#@Email   :   476063646@qq.com

import os
import requests
from io import BytesIO
from pyzbar import pyzbar
from PIL import Image, ImageEnhance
from MyQR import myqr as mq

class Qrcode():
    """二维码识别、制作工具"""

    def get_qrcode_content(self, url):
        """
        获取二维码内容
        url：图片地址(本地地址或网络地址)
        """
        if os.path.isfile(url):
            # 从本地加载二维码图片
            img = Image.open(url)
        else:
            # 从网络下载并加载二维码图片
            rq_img = requests.get(url).content
            img = Image.open(BytesIO(rq_img))
        
        # 显示图片，测试用
        # img.show()

        return pyzbar.decode(img)
    
    def qrcode_make(self, content):
        """
        制作二维码
        content：二维码内容
        """



if __name__ == '__main__':
    query = Qrcode()
    result = query.get_qrcode_content(r"D:\桌面\2.png")
    print(result)
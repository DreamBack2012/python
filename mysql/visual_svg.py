#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#@File    :   visual_svg.py
#@Time    :   2020/09/04 10:46:09
#@Author  :   Mr.W
#@Email   :   476063646@qq.com

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

class VisualSvg():
    """通过pygal画svg图"""

    def __init__(self, x_labels, y_labels, title, filename, data_title=''):
        """
        参数说明：
        x_labels，x坐标值
        y_labels，y坐标值
        title，图表标题
        filename，将保存的文件名
        data_title，数据标签，默认为空
        """
        self.x_labels = x_labels
        self.y_labels = y_labels
        self.title = title
        self.filename = filename
        self.data_title = data_title

    def draw(self, x_label_rotation=-45, show_legend=False):
        """
        画图
        参数说明：
        x_label_rotation，标签旋转角度，默认为-45度
        show_legend，是否显示图例，默认不显示
        """
        # 创建样式
        my_style = LS('#333366', base_style=LCS)    
        # 创建条形图,让标签绕x轴旋转45度,并隐藏了图例
        chart = pygal.Bar(style=my_style, x_label_rotation=x_label_rotation, 
            show_legend=show_legend) 
        # 添加标题
        chart.title = self.title
        # 设置x_labels属性
        chart.x_labels = self.x_labels
        # 添加数据
        chart.add(self.data_title, self.y_labels)
        # 生成svg图
        chart.render_to_file(self.filename)
        
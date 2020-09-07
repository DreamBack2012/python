#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#@File    :   personal_recharge.py
#@Time    :   2020/09/03 09:55:56
#@Author  :   Mr.W
#@Email   :   476063646@qq.com

import re
import calendar, time, datetime
import sys, os
from aliyun_mysql import AliyunMysql
from visual_svg import VisualSvg

class PersonalRecharge():
    """个人充值订单查询"""
    def __init__(self):
        self.db = AliyunMysql()

    def Caltime(self, date1, date2):
        """
        计算2个日期之间相差的天数
        参数说明：
        date1，第一个日期，如2020-08-03
        date2，第二个日期，如2020-09-03
        """
        date1 = time.strptime(date1, "%Y-%m-%d %H:%M:%S")
        date2 = time.strptime(date2, "%Y-%m-%d %H:%M:%S")
        date1 = datetime.datetime(date1[0],date1[1],date1[2])
        date2 = datetime.datetime(date2[0],date2[1],date2[2])
        return (date2 - date1).days

    def query_the_day(self, begin, end):
        """
        按天查询
        参数说明：
        begin，列表，开始时间
        end，列表，结束时间
        """

        # 解析日期
        date = time.strftime('%Y-%m',time.localtime(time.time())).split('-')

        # 确定日期的有效性
        begin_date = begin[0] + "-" + begin[1] + "-" + begin[2] \
                + " " + begin[3] + ":" + begin[4] + ":" + begin[5]
        end_date = end[0] + "-" + end[1] + "-" + end[2] \
                + " " + end[3] + ":" + end[4] + ":" + end[5]        
        message = ""
        if int(begin[0]) < 2018 or int(end[0]) > int(date[0]):
            message = "the year should be between 2018 and " + date[0]
        elif int(begin[1]) < 1 or int(begin[1]) > 12\
            or int(end[1]) < 1 or int(end[1]) > 12:
            message = "the mouth should be between 1 and 12"
        elif self.Caltime(begin_date, end_date) > 60:
            message = "the difference of days must not be greater than 60 days"
        
        if len(message) > 0:
            return -1
        
        # 组装sql查询语句
        sql = "SELECT FROM_UNIXTIME(create_time, '%Y-%m-%d') as date, SUM(amount) as a \
FROM recharge_order \
WHERE `status` = '1' AND amount > 0 \
AND create_time >= UNIX_TIMESTAMP(\"begin\") \
AND create_time < UNIX_TIMESTAMP(\"end\") \
GROUP BY date \
ORDER BY date ASC;"
        sql = sql.replace("begin", begin_date)
        sql = sql.replace("end", end_date)

        # 进行查询
        results = self.db.query(sql)

        # 结果分析
        dates, amounts = [], []
        for i in range(len(results)):
            dates.append(results[i]["date"])
            amounts.append(round(results[i]["a"], 2)) # 保留2位有效数字

        # 画树状图
        if begin[0] != end[0] or begin[1] != end[1]:
            title = "个人充值订单：" + begin[0] \
                + str('{:02}'.format(int(begin[1]))) \
                + str('{:02}'.format(int(begin[2]))) \
                + "-" + end[0] \
                + str('{:02}'.format(int(end[1]))) \
                + str('{:02}'.format(int(end[2]))) 
        else:
            print(begin[0])
            print(begin[1])
            title = "个人充值订单：" + begin[0] \
                + str('{:02}'.format(int(begin[1])))          
        filename = title.replace("：", "") + ".svg"
        filename = os.path.join(sys.path[0], filename)
        print(filename)
        visual = VisualSvg(dates, amounts, title, filename)
        visual.draw()

    def query_the_mouth(self, begin_year, end_year):
        """
        按月查询
        参数说明：
        begin，要查询的开始年份
        end，要查询的结束年份
        """
        # 获取当前年月
        date = time.strftime('%Y-%m',time.localtime(time.time())).split('-')
        if begin_year < 2018 or end_year > int(date[0]):
                print("the year should be between 2018 and " + date[0])
                return -1
        
        # 组装sql查询语句
        sql = "SELECT FROM_UNIXTIME(create_time, '%Y-%m') as date, SUM(amount) as a \
FROM recharge_order \
WHERE `status` = '1' AND amount > 0 \
AND create_time >= UNIX_TIMESTAMP(\"begin\") \
AND create_time < UNIX_TIMESTAMP(\"end\") \
GROUP BY date \
ORDER BY date ASC;"
        begin = str(begin_year) + "-01-01 00:00:00"
        if end_year == int(date[0]):
            # 查询的月份不能超过当前月份
            end = str(end_year) + "-" + str(int(date[1]) + 1) + "-01 00:00:00"
        else:
            end = str(end_year + 1) + "-01-01 00:00:00"

        sql = sql.replace("begin", begin)
        sql = sql.replace("end", end)

        # 进行查询
        results = self.db.query(sql)

        # 结果分析
        dates, amounts = [], []
        for i in range(len(results)):
            dates.append(results[i]["date"])
            amounts.append(round(results[i]["a"], 2)) # 保留2位有效数字

        # 画树状图
        if(begin_year == end_year):
            title = "个人充值订单：" + str(end_year)
        else:
            title = "个人充值订单：" + str(begin_year) + "-" + str(end_year)
        filename = title.replace("：", "") + ".svg"
        filename = os.path.join(sys.path[0], filename)
        print(filename)
        visual = VisualSvg(dates, amounts, title, filename)
        visual.draw()

    def query_the_year(self, begin_year, end_year):
        """
        按年查询，且不能是同一年
        参数说明：
        begin，要查询的开始年份
        end，要查询的结束年份
        """
        # 获取当前年月
        date = time.strftime('%Y-%m',time.localtime(time.time())).split('-')
        if begin_year < 2018 or end_year > int(date[0]) or begin_year == end_year:
                print("the year should be between 2018 and " + date[0])
                return -1
        
        # 组装sql查询语句
        sql = "SELECT FROM_UNIXTIME(create_time, '%Y') as date, SUM(amount) as a \
FROM recharge_order \
WHERE `status` = '1' AND amount > 0 \
AND create_time >= UNIX_TIMESTAMP(\"begin\") \
AND create_time < UNIX_TIMESTAMP(\"end\") \
GROUP BY date \
ORDER BY date ASC;"
        begin = str(begin_year) + "-01-01 00:00:00"
        end = str(end_year + 1) + "-01-01 00:00:00"
        sql = sql.replace("begin", begin)
        sql = sql.replace("end", end)

        # 进行查询
        results = self.db.query(sql)

        # 结果分析
        dates, amounts = [], []
        for i in range(len(results)):
            dates.append(results[i]["date"])
            amounts.append(round(results[i]["a"], 2)) # 保留2位有效数字

        # 画树状图
        title = "个人充值订单：" + str(begin_year) + "-" + str(end_year)
        filename = title.replace("：", "") + ".svg"
        filename = os.path.join(sys.path[0], filename)
        print(filename)
        visual = VisualSvg(dates, amounts, title, filename)
        visual.draw()

    def query(self, begin, end, query_mode):
        """
        个人充值订单查询
        参数说明：
        query_mode，查询方式，字符串，可以是year/mouth/day/time中的一种，
                    分别对应，按年查询/按月查询/按天查询/按指定时间查询
        begin，开始时间，如2020-09-03 00:00:00
        end，  结束时间，如2020-09-03 23:59:59
        """
        begin = re.split('-|:| ', begin)
        end = re.split('-|:| ', end)

        # 连接数据库
        self.db.connect()

        # 数据库查询
        if query_mode == "year":
            self.query_the_year(int(begin[0]), int(end[0]))
        elif query_mode == "mouth":
            self.query_the_mouth(int(begin[0]), int(end[0]))
        elif query_mode == "day":
            self.query_the_day(begin, end)
        else:
            print("not supported")

        # 断开数据库连接
        self.db.disconnect()


if __name__ == "__main__":
    obj = PersonalRecharge()
    obj.query("2020-08-01 00:00:00", "2020-09-30 00:00:00", "day")

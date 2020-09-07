import sys
import calendar, time, datetime

def Caltime(date1, date2):
    """
    计算2个日期之间相差的天数
    参数说明：
    date1，第一个日期，如2020-08-03
    date2，第二个日期，如2020-09-03
    """
    date1 = time.strptime(date1, "%Y-%m-%d")
    date2 = time.strptime(date2, "%Y-%m-%d")
    date1 = datetime.datetime(date1[0],date1[1],date1[2])
    date2 = datetime.datetime(date2[0],date2[1],date2[2])
    return (date2 - date1).days


begin = ["2020", "9", "02", "02", "08", "03"]
end = ["2020", "09", "03"]
# print("-".join(begin))
# print(Caltime("-".join(begin), "-".join(end)))
print("{:02}".format(int(begin[1])))
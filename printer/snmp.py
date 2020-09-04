#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#@File    :   snmp.py
#@Time    :   2020/08/25 11:57:59
#@Author  :   Mr.W
#@Email   :   476063646@qq.com


from pysnmp.entity.rfc3413.oneliner import cmdgen
 
def snmpget():
  cg = cmdgen.CommandGenerator() ##获得CommandGenerator对象
  errorIndication, errorStatus, errorIndex, varBinds = cg.getCmd(
   #0代表v1,1代表v2c 
  cmdgen.CommunityData('my-agent', 'public', 1), ##社区信息，my-agent ,public 表示社区名,1表示snmp v2c版本，0为v1版本
  cmdgen.UdpTransportTarget(('192.168.70.237', 161)),##这是传输的通道，传输到IP 192.168.70.237, 端口 161上(snmp标准默认161 UDP端口)
  '.1.3.6.1.4.1.1800.5.13.2' ##传送的OID,个人认为MIB值
  )
  print str(varBinds[0][1]); ##varBinds返回是一个stulp，含有MIB值和获得值
def runit(loop=1):
  for i in range(loop):
    snmpget()
    #print i
if __name__ == "__main__":
  runit(loop=1)
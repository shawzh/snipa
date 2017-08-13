#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 下午5:20
# @Author  : Shawz
# @Site    :
# @File    : ethernetCard.py
# @Software: PyCharm



import psutil
import os
def listEthernetCard():
    netcard_info = []
    if os.name == 'nt':

        #windows下用psutil获取的网卡不对
        from scapy.all import get_windows_if_list
        interfaces = get_windows_if_list()
        for i in interfaces:
            netcard_info.append(i['name'])
        return netcard_info


    # 获取Linux所有网卡信息
    info = psutil.net_if_addrs()
    for k, v in info.items():
        for item in v:

            # 去掉本地回环
            if item[0] == 2 and not item[1] == '127.0.0.1':
                netcard_info.append(k)

    # 返回信息像这样：
    # [('wlp2s0', '192.168.1.110')]
    return netcard_info





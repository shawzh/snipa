#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 下午5:20
# @Author  : Shawz
# @Site    :
# @File    : ethernetCard.py
# @Software: PyCharm


from scapy.all import get_windows_if_list
def listEthernetCard():
    netcard_info = []
    interfaces = get_windows_if_list()
    for i in interfaces:
        netcard_info.append(i['name'])
    return netcard_info




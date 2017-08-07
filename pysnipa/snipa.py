#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 下午5:15
# @Author  : Shawz
# @Site    :
# @File    : snipa.py
# @Software: PyCharm

from scapy.all import *

def startSniff(card,count):

    pcap = sniff(iface = card, count = count)

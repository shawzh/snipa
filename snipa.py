#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 下午5:15
# @Author  : Shawz
# @Site    :
# @File    : snipa.py
# @Software: PyCharm

from scapy.all import *


class ScapySniff(object):

    def __init__(self):
        self.pcap = None

    def startSniff(self,card,count):

        self.pcap = sniff(iface = card, count = count)

    # def getData(self):
    #
    #     self.pcap=

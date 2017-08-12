#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 下午5:15
# @Author  : Shawz
# @Site    :
# @File    : snipa.py
# @Software: PyCharm

from scapy.all import *


class ScapySniff(object):

    @staticmethod
    def startSniffDeault(card):
        print("start default sniff")

        # 默认监听，每次监听3个记录，循环调用这个方法

        return sniff(iface=card, count=3)

    def startSniff(self, **kwargs):
        sniff()


        # def getData(self):
        #
        #     self.pcap=

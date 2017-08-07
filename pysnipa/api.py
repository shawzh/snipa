#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 下午5:23
# @Author  : Shawz
# @Site    :
# @File    :api.py
# @Software: PyCharm

import zerorpc
from .utils import ethernetCard
from .utils.dbUtils import dbUtils
import pysnipa.snipa as snipa
from pysnipa.config import *
import pysnipa.insertDB as insertDB



class SnipaApi(object):
    def calc(self, text):
        """based on the input text, return the int result"""
        try:
            return eval(text)
        except Exception as e:
            return 0.0

    def echo(self, text):
        """echo any text"""
        return text

    # 返回给前端网卡可选列表
    def selectCard(self):
        return ethernetCard.listEthernetCard()

    # 开始监听
    def start(self, card, count, writeDB):
        snipa.startSniff(card, count=50)

    def ana(self):
        pass

    def testDatabaseConn(self):
        dbUtils().testConn()


    def changeConfig(self,):



def parse_port():
    return str(4242)


def main():
    addr = 'tcp://127.0.0.1:' + parse_port()
    s = zerorpc.Server(SnipaApi())
    s.bind(addr)
    print('start running on {}'.format(addr))
    s.run()


if __name__ == '__main__':
    main()

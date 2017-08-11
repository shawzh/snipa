#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 下午5:23
# @Author  : Shawz
# @Site    :
# @File    :api.py
# @Software: PyCharm

import json

from config import *
import config
from snipa import ScapySniff
from utils import ethernetCard
from utils.dbUtils import dbUtils


class SnipaApi(object):


    # 返回给前端网卡可选列表
    def selectCard(self):
        return json.dumps(ethernetCard.listEthernetCard())

    # 开始监听
    def start(self, card, count, writeDB):
        ScapySniff().startSniff(card, count=50)


    def testDatabaseConn(self):
        return dbUtils().testConn()

    # TODO: not exactly sure which args need
    def getData(self):



    def changeConfig(self,json_str):
        try:
            data = json.load(json_str)
            config.URL = data.get("url")
            config.PASSWORD = data.get("pass")
            config.DATABASE = data.get("db")
            config.USER = data.get("user")
            return 'ok'
        except Exception as e:
            return 'no'


def main():


if __name__ == '__main__':
    main()

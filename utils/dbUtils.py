#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 下午5:19
# @Author  : Shawz
# @Site    :
# @File    : dbUtils.py
# @Software: PyCharm

import pymysql
import config


class dbUtils(object):

    def __init__(self):
        # 从配置文件里导入设置
        self.url = config.URL
        self.user = config.USER
        self.password = config.PASSWORD
        self.databse = config.DATABASE


    def getConn(self):
        # 获得数据库链接
        try:
            return pymysql.connect(self.url, self.user, self.password, self.databse)
        except Exception as e:
            print(e)
            return None

    def closeConn(self, db):
        #
        try:
            db.close()
            return 1
        except Exception as e:
            print(e)
            return 0



    def testConn(self):
        # 测试链接
        #  TODO: test conn not complete
       if self.getConn() != None:
           return "ok"
       return "wrong"



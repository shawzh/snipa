#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 下午5:19
# @Author  : Shawz
# @Site    :
# @File    : dbUtils.py
# @Software: PyCharm

import pymysql
import configparser

class dbUtils(object):

    def __init__(self):
        # 加载配置文件
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')


    def getConn(self):
        # 获得数据库链接
        try:
            return pymysql.connect( self.config['DATABASE']['URL'],
                                    self.config['DATABASE']['USER'],
                                    self.config['DATABASE']['PASSWORD'],
                                    self.config['DATABASE']['DATABASE'])
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

    def writeToConfigFile(self,url,databse,password,user):
        with open('config.ini', 'w') as configfile:
            self.config['DATABASE']['URL'] = url
            self.config['DATABASE']['DATABASE'] = databse
            self.config['DATABASE']['PASSWORD'] = password
            self.config['DATABASE']['USER'] = user
            self.config.write(configfile)

    def testConn(self):
        # 测试链接
        #  TODO: test conn not complete
       if self.getConn() != None:
           return "ok"
       return "wrong"



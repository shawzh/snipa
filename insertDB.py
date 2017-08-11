#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 下午9:30
# @Author  : Shawz
# @Site    : 
# @File    : insertDB.py
# @Software: PyCharm


from utils.dbUtils import *


def insert(**msg):
    conn = dbUtils().getConn()
    cur = conn.cursor()
    cur.execute("insert into PACKETS_REC VALUES (%s,%s)" % msg.get("name"),msg.get("type"))
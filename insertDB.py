#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 下午9:30
# @Author  : Shawz
# @Site    : 
# @File    : insertDB.py
# @Software: PyCharm


from utils.dbUtils import *


def insert(list):
    conn = dbUtils().getConn()
    print(conn)
    cur = conn.cursor()
    for msg in list:
        sql = "insert into PACKETS_REC (dateTime, src, dst, poto, length, info) VALUES ('%s','%s','%s','%s',%s,'%s') " % \
              (msg[0],msg[1],msg[2],msg[3],msg[4],transferContent(msg[5]))
        cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def transferContent( content):
    if content is None:
        return None
    else:
        string = ""
        for c in content:
            if c == '"':
                    string += '\\\"'
            elif c == "'":
                    string += "\\\'"
            elif c == "\\":
                    string += "\\\\"
            else:
                    string += c
        return string
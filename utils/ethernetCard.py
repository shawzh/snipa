#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 下午5:20
# @Author  : Shawz
# @Site    :
# @File    : ethernetCard.py
# @Software: PyCharm

import psutil
def listEthernetCard():
    netcard_info = []

    # 获取所有网卡信息
    info = psutil.net_if_addrs()
    for k, v in info.items():
        for item in v:

            # 去掉本地回环
            if item[0] == 2 and not item[1] == '127.0.0.1':
                    netcard_info.append(k)


    # 返回信息像这样：
    # [('wlp2s0', '192.168.1.110')]
    return netcard_info



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-11 下午2:34
# @Author  : Shawz
# @Site    : 
# @File    : main_window.py
# @Software: PyCharm

import sys
import os
import PyQt5.QtCore as QtCore
from PyQt5.QtQuick import QQuickView
from PyQt5.QtWidgets import QApplication,QMainWindow
from utils import ethernetCard
import snipa



class MainWindow(QtCore.QObject):
    def __init__(self, r):
        # 重写此方法，但父类的__init__()不能被覆盖
        super().__init__()
        self.r = r
        # 初始化获取网卡列表
        self.setCard()

    # 获取本机网卡列表，返回到qt界面ComboBox
    def setCard(self):
        self.r.setCard(ethernetCard.listEthernetCard())

    # 在不指定监听参数下默认使用此方法，一次返回3条
    # @QtCore.Slot()
    # def startDefaultSniff(self):
    #     card = self.r.getCardComboCurrentText()
    #     msg = ScapySniff.startSniffDeault(card)
    #     for i in msg:
    #         print(i)

    # @QtCore.Slot()
    # def start


if __name__ == '__main__':


    # app = QApplication(sys.argv)
    # # 加载qml文件并显示GUI界面
    # view = QQuickView()
    # view.setSource(QtCore.QUrl("main.qml"))
    # view.show()
    #
    # # GUI signal与slot的传递依靠MainWindow类
    # mw = MainWindow(view.rootObject())
    # context = view.rootContext()
    # context.setContextProperty("mw", mw)
    #
    # sys.exit(app.exec_())

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = snipa.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


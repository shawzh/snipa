#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-11 下午2:34
# @Author  : Shawz
# @Site    : 
# @File    : main_window.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication,QDesktopWidget,QLabel,QComboBox)
from PyQt5.QtGui import QFont
import utils.ethernetCard as ethernetCard


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.resize(800, 600)
        self.center()
        self.setWindowTitle('Tooltips')
        self.show()



    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        #网卡选择列表
        cardCombo = QComboBox(self)
        self.addCardMsgToCombo(cardCombo)
        cardCombo.move(200,100)


        # 软件名
        lbl = QLabel(self)
        lbl.setText("Snipa")
        lbl.resize(lbl.sizeHint())
        lbl.move(100,50)



        btn = QPushButton('Start ！', self)
        btn.resize(btn.sizeHint())
        btn.move(500, 100)
        btn.clicked.connect(self.getSniffData())



    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def addCardMsgToCombo(self,combo):
        # 添加网卡列表到ComboBox
        msg = ethernetCard.listEthernetCard()
        combo.addItems(msg)

    def getSniffData(self):
        print("hello")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
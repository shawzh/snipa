# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'snipa.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
import sys, os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPicture,QPixmap
from analysis import graph
from setting import Ui_Dialog as Form
from tableService import TableService
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from sniff import Sniff
from utils.ethernetCard import listEthernetCard
from insertDB import insert
import configparser
from PIL import Image


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # 加载配置文件
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 770)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 网卡选择combobox
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(195, 40, 235, 25))
        self.comboBox.setObjectName("InterfaceComboBox")

        self.addItemsToInterfaceComboBox()

        # 欢迎label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 5, 195, 35))
        self.label.setObjectName("label")

        # 网卡显示label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 45, 160, 15))
        self.label_2.setObjectName("label_2")

        #
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 115, 415, 20))
        self.lineEdit.setObjectName("lineEdit")

        # 启动监听
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 40, 93, 25))
        self.pushButton.setObjectName("pushButton")

        # 监听pushButton按下
        self.pushButton.clicked.connect(self.OnpushButtonPressed)

        # 写入数据库
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(555, 40, 180, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.WriteIntoDBListener)

        # 显示图表1
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 76, 110, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.DisplayVbar)



        # 写入数据库
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(505, 115, 130, 16))
        self.label_3.setObjectName("label_3")

        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setColumnCount(6)
        self.tableView.setGeometry(QtCore.QRect(20, 145, 925, 225))
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.itemClicked.connect(self.outSelect)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 80, 57, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 115, 57, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 57, 16))
        self.label_5.setObjectName("label_5")

        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(635, 115, 65, 20))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.open_dialog)

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 430, 445, 385))
        self.label_9.setObjectName("label_9")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(145, 80, 75, 16))
        self.label_6.setObjectName("label_6")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(220, 80, 55, 20))
        self.spinBox.setObjectName("spinBox")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(480, 390, 465, 340))
        self.textBrowser.setObjectName("textBrowser")


        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(720, 115, 180, 16))
        self.label_8.setObjectName("label_8")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1929, 47))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionStartSniff = QtWidgets.QAction(MainWindow)
        self.actionStartSniff.setObjectName("actionStartSniff")
        self.actionEndSniff = QtWidgets.QAction(MainWindow)
        self.actionEndSniff.setObjectName("actionEndSniff")
        self.actionSaveDataToFile = QtWidgets.QAction(MainWindow)
        self.actionSaveDataToFile.setObjectName("actionSaveDataToFile")
        self.actionLoadDataFromFile = QtWidgets.QAction(MainWindow)
        self.actionLoadDataFromFile.setObjectName("actionLoadDataFromFile")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionStartSniff)
        self.menuFile.addAction(self.actionEndSniff)
        self.menuFile.addAction(self.actionSaveDataToFile)
        self.menuFile.addAction(self.actionLoadDataFromFile)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Sniff")

        self.label.setText(_translate("MainWindow", "Welcome to Snipa"))
        self.label_2.setText(_translate("MainWindow", "Aviliable Interfaces shown:"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Write into Database"))
        self.pushButton_3.setText(_translate("MainWindow", "Dispaly vbar"))
        self.label_3.setText(_translate("MainWindow", "Write into Databse:"))

        self.tableView.setHorizontalHeaderLabels(['Time', 'Source', 'Destination', 'Protocol',
                                                  'Length', 'Info'])

        self.label_4.setText(_translate("MainWindow", "Filter:"))
        self.label_5.setText(_translate("MainWindow", "Count:"))
        self.toolButton.setText(_translate("MainWindow", "Settings"))
        self.label_6.setText(_translate("MainWindow", "TimeLimit："))

        self.label_8.setText(_translate("MainWindow", "Status: " + self.config['DATABASE']['STATUS']))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionStartSniff.setText(_translate("MainWindow", "StartSniff"))
        self.actionEndSniff.setText(_translate("MainWindow", "EndSniff"))
        self.actionSaveDataToFile.setText(_translate("MainWindow", "SaveDataToFile"))
        self.actionLoadDataFromFile.setText(_translate("MainWindow", "LoadDataFromFile"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    # 提供可选网卡列表
    def addItemsToInterfaceComboBox(self):
        for card in listEthernetCard():
            self.comboBox.addItem(card)

    # 调用默认监听，一次取三条
    def OnpushButtonPressed(self):
        self.config['NETWORK']['CURRENT_CARD'] = self.comboBox.currentText()
        self.start()

    def start(self):

        args = {'count': self.lineEdit_2.text(),
                'timeLimit': self.spinBox.text(),
                'filter': self.lineEdit.text(),
                'iface': self.config['NETWORK']['CURRENT_CARD']}

        if self.lineEdit_2.text() == '' and self.spinBox.text() == '0' and self.lineEdit.text() == '':
            self.pcaps = Sniff.startDefaultSniff(self.config['NETWORK']['CURRENT_CARD'])
        else:
            s = Sniff()
            self.pcaps = s.Sniff(**args)
        table = TableService(pcaps=self.pcaps, model=self.tableView)
        table.insertDataToTable()

    def OnClickedTableItem(self):
        self.textBrowser.clicked.connect(self.OnClickedTableItem())

    def open_dialog(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form()
        dialog.ui.setupUi(dialog)
        dialog.show()
        dialog.exec_()

    def outSelect(self, Item=None):
        if Item == None:
            return
        index = self.tableView.currentIndex()
        self.createTextBrowser(index)
        #self.createTreeWidget(index)


    def createTreeWidget(self, index):
        info = self.pcaps[index.row()]
        info.psdump("test.eps")
        img = Image.open("test.eps")
        img.save("test.jpg", "JPEG")
        self.label_9.setPixmap(QPixmap("test.jpg").scaled(self.label_9.width(), self.label_9.height()))

    def createTextBrowser(self, index):
        info = self.pcaps[index.row()]
        try:
            self.textBrowser.clear()
            self.textBrowser.append(info.showdump())
        except:
            print('miss')

    def WriteIntoDBListener(self):

        rows = TableService(pcaps=self.pcaps,model=None).build()
        insert(rows)

        self.label_8.setText( "Status: " + "Successfully")

    def DisplayVbar(self):
        graph().createBarGraph()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

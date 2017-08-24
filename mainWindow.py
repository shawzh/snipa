# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'snipa.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from setting import Ui_Dialog as Form
from tableService import TableService
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QWidget,QHeaderView
from sniff import Sniff
from utils.ethernetCard import listEthernetCard
import configparser



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # 加载配置文件
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1929, 1726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 网卡选择combobox
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(390, 80, 471, 51))
        self.comboBox.setObjectName("InterfaceComboBox")

        self.addItemsToInterfaceComboBox()

        # 欢迎label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 391, 71))
        self.label.setObjectName("label")

        # 网卡显示label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 321, 31))
        self.label_2.setObjectName("label_2")

        #
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 230, 831, 39))
        self.lineEdit.setObjectName("lineEdit")

        # 启动监听
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(900, 80, 187, 51))
        self.pushButton.setObjectName("pushButton")

        # 监听pushButton按下
        self.pushButton.clicked.connect(self.OnpushButtonPressed)

        # 停止监听
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1110, 80, 187, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        # 写入数据库
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1010, 230, 261, 33))
        self.label_3.setObjectName("label_3")

        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setColumnCount(6)
        self.tableView.setGeometry(QtCore.QRect(40, 290, 1851, 551))
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 160, 119, 39))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 230, 114, 33))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 160, 114, 33))
        self.label_5.setObjectName("label_5")

        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(1270, 230, 131, 39))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.open_dialog)

        self.treeWidget_2 = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget_2.setGeometry(QtCore.QRect(40, 860, 891, 771))
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.treeWidget_2.headerItem().setText(0, "Formated Data")
        self.tableView.itemClicked.connect(self.outSelect)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 160, 151, 33))
        self.label_6.setObjectName("label_6")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(440, 160, 111, 41))
        self.spinBox.setObjectName("spinBox")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(960, 860, 931, 791))
        self.textBrowser.setObjectName("textBrowser")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(800, 160, 165, 37))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(1010, 160, 165, 37))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(1220, 160, 165, 37))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(1430, 160, 165, 37))
        self.checkBox_4.setObjectName("checkBox_4")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(610, 160, 181, 33))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1440, 230, 361, 33))
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
        self.pushButton_2.setText(_translate("MainWindow", "Pause"))
        self.label_3.setText(_translate("MainWindow", "Write into Databse:"))


        self.treeWidget_2.setHeaderLabels(['key','Value'])
        self.treeWidget_2.setColumnCount(2)

        self.tableView.setHorizontalHeaderLabels(['Time', 'Source', 'Destination', 'Protocol',
                                              'Length', 'Info'])

        self.label_4.setText(_translate("MainWindow", "Filter:"))
        self.label_5.setText(_translate("MainWindow", "Count:"))
        self.toolButton.setText(_translate("MainWindow", "Settings"))
        self.label_6.setText(_translate("MainWindow", "TimeLimit："))
        self.checkBox.setText(_translate("MainWindow", "write into database"))
        self.checkBox_2.setText(_translate("MainWindow", "only UDP"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.label_7.setText(_translate("MainWindow", "QuickConfig:"))

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
                'tcp': self.checkBox.isChecked(),
                'udp': self.checkBox_2.isChecked(),
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
        self.createTreeWidget(index)
        self.createTextBrowser(index)


    def createTreeWidget(self,index):
        info = self.pcaps[index.row()]

        root1 = QTreeWidgetItem(self.treeWidget_2)
        root2 = QTreeWidgetItem(self.treeWidget_2)
        root3 = QTreeWidgetItem(self.treeWidget_2)
        root4 = QTreeWidgetItem(self.treeWidget_2)
        s=info['IP'].showdump()

        root1.setText(0, info['Ether'].summary())
        info['IP'].nsummary()
        #root2.setText(0,)

        self.treeWidget_2.addTopLevelItem(root1)
        self.treeWidget_2.addTopLevelItem(root2)



    def createTextBrowser(self,index):
        info = self.pcaps[index.row()]
        try:
            self.pcaps.rawhexdump()
            #self.textBrowser.append()
        except:
            print('miss')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

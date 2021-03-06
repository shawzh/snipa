# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from utils.dbUtils import dbUtils


class Ui_Dialog(object):
    def setupUi(self, Dialog):

        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 200)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(45, 165, 205, 40))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 22, 57, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 57, 34, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 70, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 125, 70, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(125, 20, 140, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(125, 55, 140, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(125, 90, 140, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(125, 125, 140, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Url ："))
        self.label_2.setText(_translate("Dialog", "User："))
        self.label_3.setText(_translate("Dialog", "Password："))
        self.label_4.setText(_translate("Dialog", "Database："))

    def accept(self):
        dbUtils().writeToConfigFile( self.lineEdit.text(),
                                     self.lineEdit_4.text(),
                                     self.lineEdit_3.text(),
                                     self.lineEdit_2.text())


        self.Dialog.close()

    def reject(self):
        self.Dialog.close()



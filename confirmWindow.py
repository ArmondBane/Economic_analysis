# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Documents\Python\EconomicalAnaliz\files\confirmWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CheckOutWindow(object):
    def setupUi(self, CheckOutWindow):
        CheckOutWindow.setObjectName("CheckOutWindow")
        CheckOutWindow.resize(483, 610)
        self.centralwidget = QtWidgets.QWidget(CheckOutWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 40, 461, 501))
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setObjectName("textBrowser")
        self.confirmData = QtWidgets.QPushButton(self.centralwidget)
        self.confirmData.setGeometry(QtCore.QRect(324, 562, 141, 31))
        self.confirmData.setObjectName("confirmData")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 461, 21))
        self.label.setObjectName("label")
        CheckOutWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CheckOutWindow)
        QtCore.QMetaObject.connectSlotsByName(CheckOutWindow)

    def retranslateUi(self, CheckOutWindow):
        _translate = QtCore.QCoreApplication.translate
        CheckOutWindow.setWindowTitle(_translate("CheckOutWindow", "Экономический анализ"))
        self.confirmData.setText(_translate("CheckOutWindow", "Подтвердить данные"))
        self.label.setText(_translate("CheckOutWindow", "Проверьте правильность внесенных данных"))

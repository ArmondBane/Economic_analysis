# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Documents\Python\EconomicalAnaliz\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.loadFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadFileButton.setEnabled(True)
        self.loadFileButton.setGeometry(QtCore.QRect(230, 340, 151, 31))
        self.loadFileButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.loadFileButton.setObjectName("loadFileButton")
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(0, 0, 601, 41))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(14)
        self.mainLabel.setFont(font)
        self.mainLabel.setScaledContents(False)
        self.mainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLabel.setWordWrap(False)
        self.mainLabel.setObjectName("mainLabel")
        self.mainLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel_2.setGeometry(QtCore.QRect(0, 40, 601, 41))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(14)
        self.mainLabel_2.setFont(font)
        self.mainLabel_2.setScaledContents(False)
        self.mainLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLabel_2.setWordWrap(False)
        self.mainLabel_2.setObjectName("mainLabel_2")
        self.mainLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel_3.setGeometry(QtCore.QRect(0, 290, 601, 41))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(10)
        self.mainLabel_3.setFont(font)
        self.mainLabel_3.setScaledContents(False)
        self.mainLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLabel_3.setWordWrap(False)
        self.mainLabel_3.setObjectName("mainLabel_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Экономический анализ"))
        self.loadFileButton.setText(_translate("MainWindow", "Загрузить файл"))
        self.mainLabel.setText(_translate("MainWindow", "Добро пожаловать в программу"))
        self.mainLabel_2.setText(_translate("MainWindow", "Применение машинного обучения в экономическом анализе"))
        self.mainLabel_3.setText(_translate("MainWindow", "Чтобы начать - загрузите файл PDF вашей экономической отчетности"))
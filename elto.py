# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sedykhgi\Documents\ptn\elto.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(150, 220)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(150, 220))
        MainWindow.setMaximumSize(QtCore.QSize(150, 220))
        MainWindow.setBaseSize(QtCore.QSize(400, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 155, 203))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LoginEdit = QtWidgets.QLineEdit(self.groupBox)
        self.LoginEdit.setObjectName("LoginEdit")
        self.verticalLayout_3.addWidget(self.LoginEdit)
        self.PasswordEdit = QtWidgets.QLineEdit(self.groupBox)
        self.PasswordEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.PasswordEdit.setObjectName("PasswordEdit")
        self.verticalLayout_3.addWidget(self.PasswordEdit)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.OpenButton = QtWidgets.QPushButton(self.groupBox_2)
        self.OpenButton.setObjectName("OpenButton")
        self.verticalLayout.addWidget(self.OpenButton)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ELTO"))
        self.groupBox.setTitle(_translate("MainWindow", "Авторизация"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Выполнить"))
        self.OpenButton.setText(_translate("MainWindow", "Выбрать Файл"))
        self.pushButton.setText(_translate("MainWindow", "Загрузить"))
        self.pushButton_2.setText(_translate("MainWindow", "Выход"))


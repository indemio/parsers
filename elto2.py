# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\elto2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(508, 280)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.settside = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settside.sizePolicy().hasHeightForWidth())
        self.settside.setSizePolicy(sizePolicy)
        self.settside.setMinimumSize(QtCore.QSize(0, 291))
        self.settside.setMaximumSize(QtCore.QSize(16777215, 291))
        self.settside.setObjectName("settside")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.settside)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.settside)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addrEdit = QtWidgets.QLineEdit(self.groupBox)
        self.addrEdit.setObjectName("addrEdit")
        self.verticalLayout.addWidget(self.addrEdit)
        self.serviceEdit = QtWidgets.QLineEdit(self.groupBox)
        self.serviceEdit.setEnabled(False)
        self.serviceEdit.setObjectName("serviceEdit")
        self.verticalLayout.addWidget(self.serviceEdit)
        self.loginEdit = QtWidgets.QLineEdit(self.groupBox)
        self.loginEdit.setEnabled(False)
        self.loginEdit.setObjectName("loginEdit")
        self.verticalLayout.addWidget(self.loginEdit)
        self.passwordEdit = QtWidgets.QLineEdit(self.groupBox)
        self.passwordEdit.setEnabled(False)
        self.passwordEdit.setInputMask("")
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.verticalLayout.addWidget(self.passwordEdit)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.settside)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setEnabled(False)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.listEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.listEdit.setEnabled(False)
        self.listEdit.setObjectName("listEdit")
        self.listEdit.setText("Лист1")
        self.verticalLayout_2.addWidget(self.listEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileButton = QtWidgets.QPushButton(self.groupBox_2)
        self.fileButton.setObjectName("fileButton")
        self.fileButton.setEnabled(False)
        self.horizontalLayout.addWidget(self.fileButton)
        self.runButton = QtWidgets.QPushButton(self.groupBox_2)
        self.runButton.setEnabled(False)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout.addWidget(self.runButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.exitButton = QtWidgets.QPushButton(self.groupBox_2)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout_2.addWidget(self.exitButton)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addWidget(self.settside)
        self.tabside = QtWidgets.QWidget(self.centralwidget)
        self.tabside.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabside.sizePolicy().hasHeightForWidth())
        self.tabside.setSizePolicy(sizePolicy)
        self.tabside.setMinimumSize(QtCore.QSize(512, 291))
        self.tabside.setMaximumSize(QtCore.QSize(16777215, 291))
        self.tabside.setObjectName("tabside")
        self.tabside.hide()
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tabside)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tabside)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableView = QtWidgets.QTableView(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_4.addWidget(self.tableView)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.horizontalLayout_2.addWidget(self.tabside)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exitButton.clicked.connect(MainWindow.close)
        self.addrEdit.textChanged.connect(lambda: self.serviceEdit.setEnabled(True))
        self.serviceEdit.textChanged.connect(lambda: self.loginEdit.setEnabled(True))
        self.loginEdit.textChanged.connect(lambda: self.passwordEdit.setEnabled(True))
        self.passwordEdit.textChanged.connect(lambda: self.fileButton.setEnabled(True))
        self.passwordEdit.textChanged.connect(lambda: self.checkBox.setEnabled(True))
        self.checkBox.toggled['bool'].connect(self.listEdit.setEnabled)
        #self.listEdit.setEnabled(False).connect()
        #self.centralwidget.resize(self.settside.sizeHint()+self.tabside.sizeHint())
        MainWindow.resize(self.centralwidget.sizeHint())
        #MainWindow.setFixedSize(self.centralwidget.sizeHint())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ELTO"))
        self.groupBox.setTitle(_translate("MainWindow", "Авторизация"))
        self.addrEdit.setPlaceholderText(_translate("MainWindow", "Введите адрес сервера"))
        self.serviceEdit.setPlaceholderText(_translate("MainWindow", "Введите имя сервиса"))
        self.loginEdit.setPlaceholderText(_translate("MainWindow", "Введите имя пользователя"))
        self.passwordEdit.setPlaceholderText(_translate("MainWindow", "Введите пароль"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Выполнить"))
        self.checkBox.setText(_translate("MainWindow", "Имя загружаемого листа отличается от"))
        self.listEdit.setPlaceholderText(_translate("MainWindow", "Лист1"))
        self.fileButton.setText(_translate("MainWindow", "Выбрать Файл"))
        self.runButton.setText(_translate("MainWindow", "Загрузить"))
        self.exitButton.setText(_translate("MainWindow", "Выход"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Окно предпросмотра"))

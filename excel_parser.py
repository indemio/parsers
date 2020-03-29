import sys
import platform
import pandas as pd
import sqlite3
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from elto import Ui_MainWindow
import cx_Oracle


cur = None
get = ''

class Elto(QtWidgets.QMainWindow):


    def __init__(self):
        super(Elto, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.OpenButton.clicked.connect(self.open_dialog)
        self.ui.pushButton.clicked.connect(self.parser)


    def open_dialog(self):
        global get
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Temp\\', "XLSX files (*.xls *.xlsx)")[0]
        get = get.replace('', name)
        get = get.replace('/', '\\')
        self.ui.FileLine.setText(get)
        if self.ui.FileLine.textChanged is True:
        self.ui.pushButton.setEnabled()

        #if get.find('.xls*') is True:
        #self.ui.FileLine.setText(get).connect(self.ui.pushButton2.setEnabled(True))



    def connector(self):
        global cur
        conn = None
        try:
            dsn_tns = cx_Oracle.makedsn(self.ui.ServerEdit.text(), '1521', service_name=self.ui.ServiceEdit.text())
            conn = cx_Oracle.connect(user=self.ui.LoginEdit.text(), password=self.ui.PasswordEdit.text(), dsn=dsn_tns)
        except cx_Oracle.Error as error:
            print("Соединение не установлено", error)
    # try:
    #     conn = sqlite3.connect(db_name)
    # except sqlite3.Error as error:
    #     print("Соединение не установлено", error)
    # cur = conn.cursor()
    # return conn


    def parser(self):
        conn = self.connector()
        tabname = os.path.splitext(get)[0]
        try:
            if tabname.find('('):
                tabname=tabname.replace('(','')
            if tabname.find(')'):
                tabname = tabname.replace(')', '')
        except:
            pass
        print(tabname)
        raw_data= pd.read_excel(xlsx_file, sheet_name='Лист1')
        raw_data.to_sql(name=tabname,con=conn,if_exists='replace')
        conn.commit()
        conn.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Elto()
    window.show()
    sys.exit(app.exec_())

# def main():
#     parser("C:/Temp/Z_1C_(02052018-06052018)/Z_1C_(01052018).xlsx")
# main()

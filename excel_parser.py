import sys
import platform
import pandas as pd
import sqlite3
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from elto import Ui_MainWindow


cur = None
get = ''

class Elto(QtWidgets.QMainWindow):


    def __init__(self):
        super(Elto, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.OpenButton.clicked.connect(self.open_dialog)


    def open_dialog(self):
        global get
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Temp\\', "XLSX files (*.xls *.xlsx)")[0]
        get = get.replace('', name)
        get = get.replace('/', '\\')


def connector (db_name):
    global cur
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print("Соединение не установлено", error)
    cur = conn.cursor()
    return conn


def parser(xlsx_file):
    conn = connector('xlsdb.db')
    tabname = os.path.splitext(xlsx_file)[0]
    tabname=tabname.replace('(','')
    tabname = tabname.replace(')', '')
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

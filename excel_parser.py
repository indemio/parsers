import sys
import platform
import pandas as pd
import sqlite3
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QAbstractTableModel, Qt
from elto2 import Ui_MainWindow
import cx_Oracle


cur = None
get = ''


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

class Elto(QtWidgets.QMainWindow):


    def __init__(self):
        super(Elto, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.fileButton.clicked.connect(self.open_dialog)
        self.ui.runButton.clicked.connect(self.parser)



    def open_dialog(self):
        global get
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Temp\\', "XLSX files (*.xls *.xlsx)")[0]
        #get = open(name, 'r')
        #get = get.replace('', name)
        # get = get.replace('/', '\\')
        #with name:
    #         data=get.read()
        if name !='':
            self.ui.runButton.setEnabled(True)
            self.ui.tabside.show()
            sname="Лист1"
            if self.ui.checkBox.isChecked() == True:
                df = pd.read_excel(name, sheet_name=self.ui.listEdit.text())
            else:
                df=pd.read_excel(name, sheet_name=sname)
            model = pandasModel(df)
            self.ui.tableView.setModel(model)
            self.ui.tableView.show()

    def connector (self):
        global cur
        conn = None
        try:
            dsn_tns = cx_Oracle.makedsn(self.ui.addrEdit.text(), '1521', service_name=self.ui.serviceEdit.text())
            conn = cx_Oracle.connect(user=self.ui.loginEdit.text(), password=self.ui.passwordEdit.text(), dsn=dsn_tns)
        except cx_Oracle.Error as error:
            print("Соединение не установлено", error)
        # try:
        #     conn = sqlite3.connect(db_name)
        # except sqlite3.Error as error:
        #     print("Соединение не установлено", error)
        # cur = conn.cursor()
        # return conn


    def parser(self, xlsx_file):
        conn = self.connector()
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

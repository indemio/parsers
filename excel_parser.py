import sys
import platform
import pandas as pd
import sqlite3
import os
from sqlalchemy import types, create_engine, exc
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QAbstractTableModel, Qt
from elto2 import Ui_MainWindow
import cx_Oracle

os.environ['NLS_LANG'] = 'American_America.CL8MSWIN1251'
cur = None
#get = ''
name = ''
sname=''


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


    def error_resolver(self, error, title):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(str(error))
        msg.setWindowTitle(title)
        return msg


    def df_loader(self, name, sname):
        try:
            df = pd.read_excel(name, sheet_name=sname)
            return df
        except:
            return None

    def open_dialog(self):
        global name
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Temp\\', "XLSX files (*.xls *.xlsx)")[0]
        if name !='':
            self.table_viewer(name)


    def table_viewer(self, name):
        global sname
        if self.ui.checkBox.isChecked() == True:
            sname=self.ui.listEdit.text()
        else:
            sname="Лист1"
        df =self.df_loader(name,sname)
        if df is not None:
            try:
                model = pandasModel(df)
                self.ui.tableView.setModel(model)
                self.ui.tableView.show()
                self.ui.runButton.setEnabled(True)
                self.ui.tabside.show()
            except:
                pass
        else:
            msg=self.error_resolver("Имя загружаемого листа отличается от "+sname,"Ошибка")
            msg.exec_()


    def connector (self):
        global cur
        conn = None
        try:
            conn = create_engine('oracle+cx_oracle://'+self.ui.loginEdit.text()+':'+self.ui.passwordEdit.text()+
                                 '@'+self.ui.addrEdit.text()+':1521/?service_name='+self.ui.serviceEdit.text())
            conn.execute('select sysdate from dual').fetchall()
            return conn, None
        except exc.DatabaseError as error:
            return None, error
        # try:
        #     conn = sqlite3.connect(db_name)
        # except sqlite3.Error as error:
        #     print("Соединение не установлено", error)
        # cur = conn.cursor()
        # return conn


    def parser(self):
        global name
        global sname
        conn, error = self.connector()
        if conn is not None:
            try:
                tabname = os.path.split(name)[1]
                tabname = os.path.splitext(tabname)[0]
                tabname = tabname.replace('(','')
                tabname = tabname.replace(')', '')
                df=pd.read_excel(name, sheet_name=sname)
                dtyp = {c: types.VARCHAR(df[c].str.len().max())
                        for c in df.columns[df.dtypes == 'object'].tolist()}
                df.to_sql(name=tabname,con=conn,if_exists='replace',dtype=dtyp)
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Запись выполнена успешно')
                msg.setWindowTitle('Успех')
                msg.exec_()
            except exc.DatabaseError as error:
                msg=self.error_resolver(error,"Запись не выполнена")
                msg.exec_()
                #pass
        else:
            msg=self.error_resolver(error,"Соединение не установлено")
            msg.show()





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Elto()
    window.show()
    sys.exit(app.exec_())

import pandas as pd
import sqlite3
import os
from sqlite3 import Error

cur = None


def connector (db_name):
    global cur
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print("Соединение не установлено", error)
    cur = conn.cursor()
    return conn


# def db_creator(NameTable, Data):
#     try:
#         sql1 = 'create table if not exists {0} ({1})'.format(NameTable, Data.columns)
#         cur.executemany(sql, Data)
#
#     except sqlite3.Error as error:
#         print("Таблица не создана", error)


def InserDataSQL(conn, NameTable, Data):
    cur=conn.cursor()
    if not len(Data):
        return
    try:
        # for row in cur.execute("select * from "+NameTable):
        #     print(row)
        cur.execute('create table if not exists {0} ({1})'.format(NameTable, Data.columns))
        sql = 'INSERT OR REPLACE INTO {0} VALUES ({1})'.format(NameTable, ('?,' * len(Data.columns))[:-1])
        cur.executemany(sql, Data)
    except sqlite3.Error as error:
        print("Ошибка", error)


def parser(xlsx_file):
    conn = connector('xlsdb.db')
    raw_data= pd.read_excel(xlsx_file, sheet_name='Лист1')
    tabname = os.path.splitext(xlsx_file)[0]
    conn = connector('xlsdb.db')
    #db_creator(tabname, raw_data)
    InserDataSQL(conn, tabname, raw_data)
    conn.commit()
    conn.close()

def main():
    parser("test.xlsx")
    # conn=connector('xlsdb.db')
    # conn.commit()
    # conn.close()
main()

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


def parser(xlsx_file):
    conn = connector('xlsdb.db')
    tabname = os.path.splitext(xlsx_file)[0]
    tabname=tabname.replace('(','')
    tabname = tabname.replace(')', '')
    raw_data= pd.read_excel(xlsx_file, sheet_name='Лист1')
    raw_data.to_sql(name=tabname,con=conn,if_exists='replace')
    conn.commit()
    conn.close()


def main():
    parser("C:/Temp/Z_1C_(02052018-06052018)/Z_1C_(01052018).xlsx")
main()

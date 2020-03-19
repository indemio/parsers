import sqlite3
from xml.etree import cElementTree as ET
from sqlite3 import Error
import cx_Oracle
from cx_Oracle import Error

try:
    dsn_tns = cx_Oracle.makedsn('10.10.1.20', '1521', service_name='KGOK')
    conn = cx_Oracle.connect(user=r'excel', password='q1w2e3', dsn=dsn_tns)
except cx_Oracle.Error as error:
        print("Соединение не установлено", error)
cur = None

def connector(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
    except sqlite3.Error as error:
        print("Соединение не установлено", error)

    return conn


def InserDataSQL(NameTable, Data):
    if not len(Data):
        return
    try:
        #sql_create='create table if not exists tempTab (UIN PRIMARY KEY, {0})'.format(Data.)
        sql = 'INSERT OR REPLACE INTO {0} VALUES ({1})'.format(NameTable, ('?,' * len(Data[0]))[:-1])
        #cur.excutemany(sql_create, Data)
        cur.executemany(sql, Data)
    except sqlite3.Error as error:
        print("Ошибка", error)


def parser(xmlFile, conn):
    global cur

    cur = conn.cursor()
    tree=ET.parse(xmlFile)
    root=tree.getroot()
    parse_list=list()
    tupol=dict()
    ignore = ('ДополнительнаяИнформация', 'Контакты', 'ЮридическийАдрес', 'ПочтовыйАдрес')
    for child in root:
        for book in child:
            contract = list()
            uin = ''
            for atribut in book:
                tag = atribut.tag.replace('{http://www.mechel.corp/counterparties}', '')

                if len(atribut):
                    if tag in tupol:
                        value = tupol.pop(tag)
                    else:
                        value = list()

                    dop_list = list()
                    dop_list.append(uin)

                    for excl1 in atribut:
                         dop_list.append(excl1.text)

                    value.append(dop_list)
                    tupol.update({tag: value})
                elif tag in ignore:
                    continue
                else:
                    contract.append(atribut.text)
                    if tag == 'УИН':
                        uin = atribut.text

            parse_list.append(contract)
    for key, value in tupol.items():
        print(key)
    InserDataSQL('tempTab' , parse_list)
    InserDataSQL('tempTab2', tupol['ДополнительнаяИнформация'])
    InserDataSQL('tempTab3', tupol['Контакты'])
    InserDataSQL('tempTab4', tupol['ЮридическийАдрес'])
    InserDataSQL('tempTab5', tupol['ПочтовыйАдрес'])


def main():
    conn=connector("pythonsqlite.db")
    parser("20200313-165646import.xml",conn)
    conn.commit()
    conn.close()
main()
# if __name__ == "__main__":
#     parser("C:/temp/20200313-165646import.xml")
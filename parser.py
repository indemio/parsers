from xml.etree import cElementTree as ET
import cx_Oracle
from cx_Oracle import Error
import os


os.environ['NLS_LANG'] = 'American_America.CL8MSWIN1251'
cur = None


def connector():
    global cur

    conn = None
    try:
        dsn_tns = cx_Oracle.makedsn('', '1521', service_name='')
        conn = cx_Oracle.connect(user=r'', password='', dsn=dsn_tns)
        
    except cx_Oracle.Error as error:
        print("Соединение не установлено", error)
    cur = conn.cursor()
    return conn


def InserDataSQL(NameTable, Data):
    if not len(Data):
        return
    try:
        for row in cur.execute("select * from "+NameTable):
            print(row)
        cur.execute('delete from '+NameTable)
        sql = 'INSERT INTO {0} VALUES (:{1})'.format(NameTable, ',:'.join(map(str, range(1, len(Data[0])+1))))
        cur.executemany(sql, Data)
    except cx_Oracle.Error as error:
        print("Ошибка", error)


def parser(xmlFile, conn):
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


    InserDataSQL('SRNT_ERP_AGNLIST' , parse_list)
    InserDataSQL('SRNT_ERP_AGNLIST_DOPINFO', tupol['ДополнительнаяИнформация'])
    InserDataSQL('SRNT_ERP_AGNLIST_PHONE', tupol['Контакты'])
    InserDataSQL('SRNT_ERP_AGNLIST_JURADR', tupol['ЮридическийАдрес'])
    InserDataSQL('SRNT_ERP_AGNLIST_POSTADR', tupol['ПочтовыйАдрес'])


def main():
    conn=connector()
    parser("20200313-165646import.xml",conn)
    conn.commit()
    conn.close()
main()

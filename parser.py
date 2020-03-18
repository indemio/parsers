import sqlite3
from xml.etree import cElementTree as ET
from sqlite3 import Error


def connector(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
    except sqlite3.Error as error:
        print("Соединение не установлено", error)

    return conn


def parser(xmlFile, conn):
    cur = conn.cursor()
    tree=ET.parse(xmlFile)
    root=tree.getroot()
    parse_list=list()
    tupol=dict()
    for child in root:
        for book in child:
            contract = list()
            uin = ''
            for atribut in book:
                if len(atribut):
                    tag=atribut.tag.replace('{http://www.mechel.corp/counterparties}','')

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
                else:
                    contract.append(atribut.text)
                    if atribut.tag == '{http://www.mechel.corp/counterparties}УИН':
                        uin = atribut.text

            parse_list.append(contract)
    sql_param1=list()
    sql_param2 = list()
    sql_param3 = list()
    sql_param4 = list()

    # for dop in tupol['ДополнительнаяИнформация']:
    #     #sql_param1.append(dop)
    #     print(dop.)
    # for kon in tupol['Контакты']:
    # #     sql_param2.append(kon)
    #      print(sql_param2)
    # #print(sql_param1)
    ind=0
    for ind in tupol['ДополнительнаяИнформация'].index(0):
        ind=ind+1
        print(tupol.values())
    try:
        sql = 'INSERT OR REPLACE INTO {0} VALUES ({1})'
        cur.execute(sql.format('tempTab',  ('?,' * len(parse_list[0]))[:-1]), parse_list[0])
        #for dop in tupol['ДополнительнаяИнформация']:
        cur.executemany(sql.format('tempTab2', ('?,' * len(tupol['ДополнительнаяИнформация']))[:-1]), tupol.items()['ДополнительнаяИнформация'])
        cur.execute(sql.format('tempTab3', ('?,' * len(tupol['Контакты']))[:-1]), tupol['Контакты'])
        cur.execute(sql.format('tempTab4', ('?,' * len(tupol['ЮридическийАдрес']))[:-1]), tupol['ЮридическийАдрес'])
        cur.execute(sql.format('tempTab5', ('?,' * len(tupol['ПочтовыйАдрес']))[:-1]), tupol['ПочтовыйАдрес'])

        # sql = '''INSERT OR REPLACE INTO tempTab VALUES (
        #     {0}
        #     );
        # INSERT OR REPLACE INTO tempTab2 VALUES (
        #     {1}
        #     );
        # INSERT OR REPLACE INTO tempTab3 VALUES (
        #     {2}
        #     );
        # INSERT OR REPLACE INTO tempTab4 VALUES (
        #     {3}
        #     );
        # INSERT OR REPLACE INTO tempTab5 VALUES (
        #     {4}
        #     )
        # '''.format(('?,'*len(parse_list[0]))[:-1],
        #            ('?,'*len(tupol['ДополнительнаяИнформация']))[:-1],
        #            ('?,'*len(tupol['Контакты']))[:-1],
        #            ('?,'*len(tupol['ЮридическийАдрес']))[:-1],
        #            ('?,'*len(tupol['ПочтовыйАдрес']))[:-1])
        #
        # cur.executescript(sql, parse_list,
        #                   tupol['ДополнительнаяИнформация'],
        #                   tupol['Контакты'],
        #                   tupol['ЮридическийАдрес'],
        #                   tupol['ПочтовыйАдрес'])
    except sqlite3.Error as error:
        print("Ошибка", error)
    print(parse_list[0])
    # print(parse_list[1])
    print(tupol['ДополнительнаяИнформация'][0])
    # print(tupol['Контакты'])
    # print(tupol['ЮридическийАдрес'])
    # print(tupol['ПочтовыйАдрес'])


def main():
    conn=connector("pythonsqlite.db")
    parser("20200313-165646import.xml",conn)
    conn.commit()
    conn.close()
main()
# if __name__ == "__main__":
#     parser("C:/temp/20200313-165646import.xml")
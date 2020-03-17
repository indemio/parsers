import sqlite3
from xml.etree import cElementTree as ET
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def parser(xmlFile):
    tree=ET.parse(xmlFile)
    root=tree.getroot()
    parse_list={}
    for books in root:
        for book in books:
            parse_list[book.tag]=book.text
        for key in parse_list:
            print(parse_list[key])


if __name__ == "__main__":
    parser("example.xml")
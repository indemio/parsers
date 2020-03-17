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
    parse_list=dict()
    for book in root.findall('book'):
        author=book.find('author').text
        title=book.find('title').text
        genre=book.find('genre').text
        price=book.find('price').text
        publish_date=book.find('publish_date').text
        description=book.find('description').text
        parse_list.update(book[('author',author)])
        #, book[title], book[genre], book[price], book[publish_date], book[description]))
        print(parse_list)


if __name__ == "__main__":
    parser("example.xml")
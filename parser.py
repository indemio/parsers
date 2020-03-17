from xml.etree import cElementTree as ET


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
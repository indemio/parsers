from xml.etree import cElementTree as ElementTree
import sqlite3

class XmlDictConfig(dict):
    def __init__(self, parent_element):
        super().__init__()
        if parent_element.items():
            self.updateShim( dict(parent_element.items()) )
        for element in parent_element:
            if len(element):
                aDict = XmlDictConfig(element)
                self.updateShim({element.tag: aDict})
            elif element.items():
                elementattrib= element.items()
                if element.text:
                    elementattrib.append((element.tag,element.text ))
                self.updateShim({element.tag: dict(elementattrib)})
            else:
                self.updateShim({element.tag: element.text})


        # if parent_element.tag == '{http://www.mechel.corp/counterparties}Контрагент':
        #      print()


    def updateShim (self, aDict ):
        for key in aDict.keys():
            tag = key.replace("{http://www.mechel.corp/counterparties}", '')
            if key in self:
                value = self.pop(tag)
                if type(value) is not list:
                    listOfDicts = []
                    #listOfDicts.append(value)
                    listOfDicts.append(aDict[key])
                    self.update({tag: listOfDicts})
                else:
                    value.append(aDict[key])
                    self.update({tag: value})
            else:
                self.update({tag:aDict[key]})


def parseXML(xml_file):
    tree = ElementTree.parse(xml_file)
    root = tree.getroot()
    xmldict=XmlDictConfig(root)
    print(xmldict)


if __name__ == "__main__":
    parseXML("C:/temp/20200313-165646import.xml")




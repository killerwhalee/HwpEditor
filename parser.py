import os
import xml.etree.ElementTree as xml

#--------- HELPER CLASS ---------#

class Text:
    def __init__(self):
        self.type = None
        self.setting = {}
        self.string = ""

#---------  MAIN  CLASS ---------#

class HML:
    """
    HWP object

    HWP object is where parsed hml file gets saved.
    """

    def __init__(self, src):
        """
        Initiate HWP object
        """

        # Initiate Basic Variable
        self.xmlString = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?>'
        self.hmlTree = xml.Element

        # Initiate Head Data
        self.textList = []

        # Initiate Body Data

        self.parseFile(src)

    def iterTree(self):
        self.iterTree(self.hmlTree, 0)
    
    def iterTree(self, tree, depth):
        print("\t" * depth, tree.tag, tree.attrib, tree.text)

        for child in tree:
            self.iterTree(child, depth = depth + 1)

    def parseFile(self, src):
        """
        parseFile - Parsing hml file into xml.Element object
        """
        
        # Concatenate every line in hml file
        with open(src, "r", encoding = "UTF-8") as file:
            hmlString = ""
            for line in file:
                hmlString += line.strip()

        # <FWSPACE/> tag is special tag which treated as string.
        # To prevent parser to parse this tag, masking the tag before parsing.
        # <FWSPACE/> -> |FS| -> <FWSPACE/>
        # Parse string and save in HWPObject
        self.hmlTree = xml.fromstring(hmlString.replace("<FWSPACE/>", "|FS|"))

    def getText(self):
        """
        Get text from HML object
        """
        for paraElem in self.hmlTree.iter("P"):
            notNone = False

            for textElem in paraElem.iter("TEXT"):
                for element in textElem:
                    if element.tag == "CHAR" and element.text != None:
                        print(element.text, end = "")
                        notNone = True
                    if element.tag == "EQUATION":
                        print(f"##{element.find('SCRIPT').text}##", end = "")
                        notNone = True
            
            if notNone:
                print("")

    def addElement(self, location, value):
        """
        Get element at HML object
        """

        pass

    def setElement(self, location, value):
        """
        Set element at HML object
        """

        pass

    def __str__(self):
        """
        Print information of HML object
        """

        pass

#--------- START MODULE ---------#
if __name__ == "__main__":
    hell = HML("test_article.hml") # Enter your file location here
    hell.getText()
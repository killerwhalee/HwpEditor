import os
import xml.etree.ElementTree as xml

#--------- HELPER CLASS ---------#

class DocSetting:
    def __init__(self):
        self.beginNumber    = {}
        self.caretPos       = {}

class MapTable:
    def __init__(self):
        self.binDataList    = []
        self.faceNameList   = []
        self.borderFillList = []
        self.charShapeList  = []
        self.tabDefList     = []
        self.paraShapeList  = []
        self.styleList      = []

class CompDoc:
    def __init__(self):
        self.layoutCompatibility = {}

class Node:     # Node is for unimportant tag
    def __init__(self):
        self.name       = None
        self.attriute   = {}

class Text:
    def __init__(self):
        self.type = None
        self.setting = {}
        self.string = ""

class Paragraph:
    def __init__(self):
        self.attribute  = {}
        self.paraElem   = []    # Has element of Text.

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

        self.xmlString = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?>'

        # For Head Data
        self.docSummary         = {}
        self.docSetting         = DocSetting()
        self.mappingTable       = MapTable()
        self.compatibleDocument = CompDoc()

        # For Body Data
        self.section = None
        self.paraList = []  # This is list of paragraphs, where Paragraph is element of list.


        # For Tail Data
        self.tailString = ""    # We do not provide tail parsing yet.

        self.parseFile(src)
    
    def parseFile(self, src):
        """
        parseFile - Parsing hml file into HWP object.
        """
        
        # Concatenate every line in hml file
        with open(src, "r", encoding = "UTF-8") as file:
            hmlString = ""
            for line in file:
                hmlString += line.strip()

        # Parse string and save in HWPObject
        hmlTree = xml.fromstring(hmlString)

        # Interpreting Head part

        # Interpreting Body part

        # Interpreting Tail part
    
    def tokenize(self, src):
        """
        tokenize..wait for it
        """


    def getElement(self, location):
        """
        Get element from HWP object
        """

        pass

    def setElement(self, location, value):
        """
        Set element at HWP object
        """

        pass

    def __str__(self):
        """
        Print information of HML object
        """

        pass

#--------- START MODULE ---------#
if __name__ == "__main__":
    hell = HML(r"C:\Users\jacob\Desktop\test.hml") # Enter your file location here
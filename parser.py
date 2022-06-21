import os
import xml

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

class Text:
    def __init__(self):
        pass

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
        

        # For Tail Data

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
        # Implement here #


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

# Start module
if __name__ == "__main__":
    hell = HML(None) # Enter your file location here
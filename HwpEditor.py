import xml.etree.ElementTree as xml

#--------- HELPER CLASS ---------#

class Text:
    def __init__(self, type = None, style = {}, string = ""):
        self.type = type
        self.style = style
        self.string = string

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

        # Initiate Text Data
        self.textStrList = []

        # Initiate Head Data
        self.fontData = []
        self.styleData = []

        self.parseFile(src)

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


        # Make textStrList
        for paraElem in self.hmlTree.iter("P"):
            notNone = False

            for textElem in paraElem.iter("TEXT"):
                for element in textElem:
                    if element.tag == "CHAR" and element.text != None:
                        self.textStrList.append(Text(type = "CHAR", string = element.text))
                        notNone = True
                    if element.tag == "EQUATION":
                        self.textStrList.append(Text(type = "EQUATION", string = f"{element.find('SCRIPT').text}"))
                        notNone = True
            
            if notNone:
                self.textStrList.append(Text(type = "LINEBREAK", string = "\n"))

    def getText(self):
        """
        Get text from HML object
        """
        outputStr = ""

        for text in self.textStrList:
            if text.type == "EQUATION":
                outputStr += f"<{text.string}>"
            outputStr += text.string

        return outputStr
    
    def getTextList(self):
        """
        Get text list from HML object
        """
        outputStrList = []

        for text in self.textStrList:
            outputStrList.append(text.string)

        return outputStrList

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
    print(hell.getTextList())
    print(hell.getText())
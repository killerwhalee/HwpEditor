import xml.etree.ElementTree as xml

#--------- HELPER CLASS ---------#

class Text:
    def __init__(self, type = None, style = None, string = ""):
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
        self.fontData = {"Hangul": [], "Latin": [], "Hanja": [], "Japanese": [], "Other": [], "Symbol": [], "User": []}
        self.charshapeData = []
        self.parashapeData = []

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


        # Make fontData
        for fontfaceElem in self.hmlTree.iter("FONTFACE"):
            for fontElem in fontfaceElem.iter("FONT"):
                self.fontData[fontfaceElem.attrib["Lang"]].append((fontElem.attrib["Name"], fontElem.attrib["Type"]))

        # Make charShapeData


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

    def getText(self) -> str:
        """
        Get text from HML object
        """
        outputStr = ""

        for text in self.textStrList:
            if text.type == "EQUATION":
                outputStr += f"<{text.string}>"
            
            else:
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
    

    def iterTree(self, tree, depth = 0):
        """
        Print tabbed result of hml file.
        """
        tabStr = '\t' * depth
        string = f"{tabStr}{tree.tag} {tree.attrib} {tree.text}\n"

        for child in tree:
            string += self.iterTree(child, depth + 1)
        
        return string

#--------- START MODULE ---------#
if __name__ == "__main__":
    hell = HML("Tests/test_owldoc.hml") # Enter your file location here
    
    fire = hell.iterTree(hell.hmlTree)
    with open('parsedHML.txt', 'w', encoding = 'UTF-8') as tell:
        tell.write(fire)
    #print(hell.getTextList())
    #print(hell.getText())
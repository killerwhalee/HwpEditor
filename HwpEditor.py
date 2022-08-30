import xml.etree.ElementTree as xml
import HwpHelper as hwphelp

#--------- HELPER CLASS ---------#

class CHAR:
    def __init__(self, type = None, paraShape = None, charShape = None, string = ""):
        self.type = type
        self.paraShape = paraShape
        self.charShape = charShape
        self.string = string

class EQTN:
    def __init__(self, paraShape = None, charShape = None, string = ""):
        self.type = "EQUATION"
        self.paraShape = paraShape
        self.charShape = charShape
        self.shapeProperty = {}
        self.string = string
    
    def calcWidth(self):
        """
        calcWidth calculates and return width of equation.
        """
        pass

class CharShape:
    def __init__(self):
        self.languageShape = {
            "fontId" : [0, 0, 0, 0, 0, 0, 0], 
            "ratio" : [100, 100, 100, 100, 100, 100, 100], 
            "charSpacing" : [0, 0, 0, 0, 0, 0, 0], 
            "relSize" : [100, 100, 100, 100, 100, 100, 100], 
            "charOffset" : [0, 0, 0, 0, 0, 0, 0]
        }
        self.property = {
            "borderFillId" : 0, 
            "height" : 0,
            "shadeColor" : 0, 
            "symbolMark" : 0, 
            "textColor" : 0, 
            "useFontSpace" : False, 
            "useKerning" : False
        }
        self.fancy = []

class ParaShape:
    pass

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
        self.fontData = {
            "Hangul": [], "Latin": [], "Hanja": [], 
            "Japanese": [], "Other": [], "Symbol": [], "User": []
            }
        self.charShapeList = [None]
        self.paraShapeList = [None]

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
        for charShapeList in self.hmlTree.iter("CHARSHAPELIST"):
            for charShapeElem in charShapeList:
                charShape = CharShape()

                childMap = {
                    "FONTID" : "fontId", 
                    "RATIO" : "ratio", 
                    "CHARSPACING" : "charSpacing", 
                    "RELSIZE" : "relSize", 
                    "CHAROFFSET" : "charOffset"
                }

                attribMap = {
                    "BorderFillId" : "borderFillId", 
                    "Height" : "height", 
                    "ShadeColor" : "shadeColor", 
                    "SymMark" : "symbolMark", 
                    "TextColor" : "textColor", 
                    "UseFontSpace" : "useFontSpace", 
                    "UseKerning" : "useKerning"
                }

                for child in charShapeElem:
                    charShape.languageShape[childMap[child.tag]] = hwphelp.getLangIdList(child.attrib)

                for key in charShapeElem.attrib:
                    if key == "Id":
                        continue

                    charShape.property[attribMap[key]] = hwphelp.interpAttribute(attribMap[key], charShapeElem.attrib[key])

                self.charShapeList.append(charShape)
        
        for elem in self.charShapeList:
            if elem:
                print(elem.languageShape, elem.property)


        # Make paraShapeData


        # Make textStrList
        for paraElem in self.hmlTree.iter("P"):
            notNone = False

            for textElem in paraElem.iter("TEXT"):
                for element in textElem:
                    if element.tag == "CHAR" and element.text != None:
                        self.textStrList.append(CHAR(type = "CHAR", string = element.text))
                        notNone = True
                    if element.tag == "EQUATION":
                        self.textStrList.append(EQTN(string = f"{element.find('SCRIPT').text}"))
                        notNone = True
            
            if notNone:
                self.textStrList.append(CHAR(type = "LINEBREAK", string = "\n"))

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
    rootDir = "./Repository/Editor.hwp"
    hell = HML(f"{rootDir}/Tests/test_textcolor.hml") # Enter your file location here
    
    fire = hell.iterTree(hell.hmlTree)
    with open(f"{rootDir}/Resources/parsedHML.txt", "w", encoding = "UTF-8") as tell:
        tell.write(fire)
    #print(hell.getTextList())
    #print(hell.getText())
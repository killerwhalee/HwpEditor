import os
import xml

class HWP:
    """
    HWP object

    HWP object is where parsed hml file gets saved.
    """

    def __init__(self):
        """
        Initiate HWP object
        """
        pass

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

class Text:
    def __init__(self):
        pass

class Font:
    def __init__(self):
        pass

def parseFile(src):
    """
    parseFile - Parsing hml file into HWP object.
    """
    
    # Concatenate every line in hml file
    with open(src, "r", encoding = "UTF-8") as file:
        hmlString = ""
        for line in file:
            hmlString += line.strip()
    
    HWPObject = HWP

    # Parse string and save in HWPObject
    # Implement here #


    # return HWPObject
    return HWPObject


# Start module
if __name__ == "__main__":
    parseFile(None, None) # Enter your file location here
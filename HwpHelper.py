"""
HWP Helper

This module is library for HwpEditor module.
It provides useful function which HwpEditor can use.
"""


def getLangIdList(langId):
    """
    It gets dictionary of language id and extracts Id for each language.
    Returns list of fontId whose type is integer, not string.
    """
    resultList = []

    resultList.append(int(langId["Hangul"]))
    resultList.append(int(langId["Hanja"]))
    resultList.append(int(langId["Japanese"]))
    resultList.append(int(langId["Latin"]))
    resultList.append(int(langId["Other"]))
    resultList.append(int(langId["Symbol"]))
    resultList.append(int(langId["User"]))

    return resultList

def interpAttribute(type, data):
    """
    It interprets data for certain attribute. Since every value for key in attribute is string, which is hard to modify and manipulate.
    """

    # (str) -> (int)
    if type in ["borderFillId", "symbolMark"]:
        return int(data)
    
    # (str) -> (bool)
    if type in ["useFontSpace", "useKerning"]:
        if data == "true":
            return True
        if data == "false":
            return False
    
    # (str) -> (HexColor)
    if type in ["shadeColor", "textColor"]:
        decData = int(data)
        hexColor = [0, 0, 0, 0]

        decData, hexColor[0] = decData // 256, decData % 256
        decData, hexColor[1] = decData // 256, decData % 256
        hexColor[3], hexColor[2] = decData // 256, decData % 256

        return hexColor

if __name__ == "__main__":
    print(interpAttribute("shadeColor", "5395143"))
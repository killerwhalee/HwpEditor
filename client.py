import HwpEditor as hml

file = hml.HML("Tests/test.hml")

for text in file.textStrList:
    if text.type == "EQUATION" and "의" in text.string:
        print(text.type, text.string)
        pass
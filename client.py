import HwpEditor as hml

file = hml.HML("Tests/root test.hml")

for text in file.textStrList:
    print(text.type, text.string)


'''
for index in range(len(file.textStrList)):
    style = file.textStrList[index].style

    if style == "EQUATION":
        file.textStrList[index].string = "LEFT rmT RIGHT"
'''



#file.saveTextStrList("C:/Desktop/result.hml")
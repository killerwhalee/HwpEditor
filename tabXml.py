import xml.etree.ElementTree as xml

def tab_xml(current, parent=None, index=-1, depth=0):
    for i, node in enumerate(current):
        tab_xml(node, current, i, depth + 1)
    if parent is not None:
        if index == 0:
            parent.text = '\n' + ('\t' * depth)
        else:
            parent[index - 1].tail = '\n' + ('\t' * depth)
        if index == len(parent) - 1:
            current.tail = '\n' + ('\t' * (depth - 1))

filePath = input("enter absolute file path: ")
tree = xml.parse(filePath)
tab_xml(tree.getroot())

xml.dump(tree)
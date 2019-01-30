import xmltodict, json
import os

def inputFileName():
    print("inpit file name (ex. weather.xml)")
    fileName = input(">>> ")
    print("")
    return fileName

def readXmlFile(fileName):
    f = open(fileName)
    xmlContent = f.read()
    return xmlContent

def convertXmlToJson(xmlContent):
    global json
    xmlDict = xmltodict.parse(xmlContent)
    for i in xmlDict.keys():
        json = json.dumps(xmlDict[i])
    return json

def createJsonFile(json, fileName):
    fileName = fileName.replace('.xml', '')
    output_file = open(fileName + '.json', 'w')
    output_file.write(json)

def frameFunction(textInFrame):
    for num in range(46):
        print("#", end="")
    print("")
    print(textInFrame.center(46), end="")
    print("")
    for num in range(46):
        print("#", end="")
    print("")
    print("")

def xml2json():
    frameFunction("XML 2 JSON CONVERTER")
    fileName = inputFileName()
    xmlContent = readXmlFile(fileName)
    json = convertXmlToJson(xmlContent)
    createJsonFile(json, fileName)
    frameFunction(fileName.replace('.xml', '.json')+" created")


xml2json()
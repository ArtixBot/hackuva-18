import csv
import re

#In this file we are reading in 2 different files:
#File 1: Database file full of private info from the user
#File 2: File produced from keylogger



# #date = {"SSN" : "xxx-xx-xxxx", "email" : "xxxx@.edu", "phone" : "xxx-xxx-xxxx" }
# privateInfo = []
# #privateSSN
# #privateEmail
# #privatePhone
# dataInput = open('database.txt', 'r')
# pSSN = []
# pEmail = []
#
# data = dataInput.readlines()
# for element in data:
#     print(type(element), type(data))
#     strippedElement = element.strip("\n")
#     miniInfo = strippedElement.split(",")
#     stream.append(miniInfo)
#     print(stream)
#
# #key,date,time
datafile = open('database.txt', 'r')
# print(list(datafile))
infoPart = []
for element in datafile:
    #print(element)
    strippedElement = element.strip("\n")
    miniInfo = strippedElement.split(" ")
    #print(miniInfo)
    infoPart.append(miniInfo)
#print(infoPart)



myfile = open('log.txt', 'r')
stream = []
data = myfile.readlines()
for element in data:
    #print(type(element), type(data))
    strippedElement = element.strip("\n")
    miniInfo = strippedElement.split(",")
    stream.append(miniInfo)
print(stream)


def findOccurSSN(stream):
    listofSSN = infoPart[0]
    retIndex=[]
    for element in listofSSN:
        retIndex = [m.start() for m in re.finditer(element, stream)]

    return retIndex

def findOccurEmail(stream):
    listofEmail = infoPart[1]
    retIndex=[]
    for element in listofEmail:
        retIndex = [m.start() for m in re.finditer(element, stream)]

    return retIndex

def toSpace(x):
    if x == 'Key.space':
        return ' '
    return x

charOnlyStr = ""
def checkInfo(stream):
    stream = [list(map(lambda y: toSpace(y), l)) for l in stream]
    #print(list(stream))
    charOnly = list(map(lambda x: x[0], stream))
    charOnlyStr = "".join(map(str,charOnly))

    #print(charOnly)
    #return(charOnlyStr)
    SSNIndex = findOccurSSN(charOnlyStr)
    print(SSNIndex)
    EmailIndex = findOccurEmail(charOnlyStr)
    file = open("matches.txt", 'w')
    for index in SSNIndex:
        file.write(infoPart[index])
    for index in EmailIndex:
        file.write(infoPart[index])
    file.close()




checkInfo(stream)

#checkInfo(stream)


#     for
#     print(dates)
testInput =[[123,456], ["cow", "cattle"]]
enterString = "zxcocow"

s= testInput[0]
e= testInput[1]
for element in enterString:
    
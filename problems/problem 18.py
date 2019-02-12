print("Starting...")

import struct

def getTriangle(filename):
    triangle = [[]]
    with open(filename) as myfile:
        for line in myfile:
            line = line.rstrip('\n')
            lineArray = []
            for i in range(int((len(line)-2)/3)+1):
                lineArray.append(int(line[3*i:3*i+2]))
            triangle.append(lineArray)
    return triangle

triangle = getTriangle("triangle2.txt");
               
def constructTriangle(tri):
    #index1 is the vertical, and index2 is horizontal
    summedTriangle = []
    summedTriangle.append(tri[len(tri)-1])
    for i in range(1,len(tri)-1):
        newLine = []
        for k in range(len(tri)-i-1):
            newEntry = tri[len(tri)-i-1][k]
            newEntry+= max(summedTriangle[i-1][k], summedTriangle[i-1][k+1])
            newLine.append(newEntry)
        summedTriangle.append(newLine)
    return summedTriangle

answerTri = constructTriangle(triangle)

print(answerTri[len(answerTri)-1][0])

    

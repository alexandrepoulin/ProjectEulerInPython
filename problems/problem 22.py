print("Starting")

def countingVar(filename):
    numberOfVar = 0
    with open(filename) as myfile:
        for line in myfile:
            line = line.rstrip('\n')
            for i in range(len(line)):
                if line[i] == "\"":
                    numberOfVar += 1;
            break
    return numberOfVar/2

def newLine(x,a,b):
    if b+2 != len(x):
        return x[0:a] + x[b+2: len(x)]
    return x[0:a]

def letterValue(a):
    if a == "A":
        return 1
    if a == "B":
        return 2
    if a == "C":
        return 3
    if a == "D":
        return 4
    if a == "E":
        return 5
    if a == "F":
        return 6
    if a == "G":
        return 7
    if a == "H":
        return 8
    if a == "I":
        return 9
    if a == "J":
        return 10
    if a == "K":
        return 11
    if a == "L":
        return 12
    if a == "M":
        return 13
    if a == "N":
        return 14
    if a == "O":
        return 15
    if a == "P":
        return 16
    if a == "Q":
        return 17
    if a == "R":
        return 18
    if a == "S":
        return 19
    if a == "T":
        return 20
    if a == "U":
        return 21
    if a == "V":
        return 22
    if a == "W":
        return 23
    if a == "X":
        return 24
    if a == "Y":
        return 25
    if a == "Z":
        return 26
    return 0

def nameValue(x,c):
    sumSoFar = 0
    for i in range(0,len(x)):
        sumSoFar += letterValue(x[i])
    return sumSoFar*c

def calculateAnswer(filename):
    myfile = open(filename)
    line = myfile.readline()
    numberOfVar = countingVar(filename)
    numberOfNames = countingVar(filename)
    counter2 = 0
    answer = 0
    while counter2 < numberOfVar:
        currentFirst = "ZZZZZZZZZZZZ"
        counter = 0
        position1 = 0;
        pos1OfBest = 0;
        pos2OfBest = 0;
        for i in range(0,len(line)):
            if line[i] == "\"" and counter == 0:
                counter = 1
                position1 = i
                continue
            if line[i] == "\"" and counter == 1:
                if line[position1+1:i] < currentFirst:
                    pos1OfBest = position1
                    pos2OfBest = i
                    currentFirst = line[position1+1:i]
                counter = 0
                continue
        line = newLine(line,pos1OfBest,pos2OfBest)
        counter2 +=1
        answer += nameValue(currentFirst,counter2)
        print(counter2)
    myfile.close()
    return answer


print(calculateAnswer("names.txt"))

input("Done")

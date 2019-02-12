print("Starting")

counter = 0

file = open("poker.txt")

def nSame(x,n):
    answer = []
    for i in x:
        if x.count(i) == n and i not in answer:
            answer.append(i)
    return answer

def player1Won(x,y):
    xFlush = [x[0][1],x[1][1],x[2][1],x[3][1],x[4][1]] == [x[0][1],x[0][1],x[0][1],x[0][1],x[0][1]]
    yFlush = [y[0][1],y[1][1],y[2][1],y[3][1],y[4][1]] == [y[0][1],y[0][1],y[0][1],y[0][1],y[0][1]]

    xNumber = []
    for i in x:
        if i[0] == "A":
            xNumber.append(14)
        elif i[0] == "K":
            xNumber.append(13)
        elif i[0] == "Q":
            xNumber.append(12)
        elif i[0] == "J":
            xNumber.append(11)
        elif i[0] == "T":
            xNumber.append(10)
        else:
            xNumber.append(int(i[0]))

    yNumber = []
    for i in y:
        if i[0] == "A":
            yNumber.append(14)
        elif i[0] == "K":
            yNumber.append(13)
        elif i[0] == "Q":
            yNumber.append(12)
        elif i[0] == "J":
            yNumber.append(11)
        elif i[0] == "T":
            yNumber.append(10)
        else:
            yNumber.append(int(i[0]))

    xNumber.sort()
    yNumber.sort()

    xStraight = xNumber == [xNumber[0],xNumber[0]+1,xNumber[0]+2,xNumber[0]+3,xNumber[0]+4]
    yStraight = yNumber == [yNumber[0],yNumber[0]+1,yNumber[0]+2,yNumber[0]+3,yNumber[0]+4]

    if xStraight and xFlush and (not yStraight or not yFlush or yNumber[4]<xNumber[4]):
        return not yStraight or not yFlush or yNumber[4]<xNumber[4]
    if yStraight and yFlush and (not yStraight or not yFlush or yNumber[4]>xNumber[4]):
        return False


    x4number = nSame(xNumber,4)
    x4oak = len(x4number) != 0

    y4number = nSame(yNumber,4)
    y4oak = len(y4number) != 0

    if x4oak:
        if y4oak:
            return x4number[0] > y4number [0]
        return True
    elif y4oak:
        return False
    

    xTriples = nSame(xNumber,3)
    xhasTriple = len(xTriples) != 0
    xDouble = nSame(xNumber,2)
    xhasDouble = len(xDouble) != 0
    yTriples = nSame(yNumber,3)
    yhasTriple = len(yTriples) != 0
    yDouble = nSame(yNumber,2)
    yhasDouble = len(yDouble) != 0

    if xhasTriple and xhasDouble:
        if not yhasTriple or not yhasDouble:
            return True
        return xTriples[0] > yTriples[0]
    elif yhasTriple and yhasDouble:
        return False
    
    if xFlush:
        if yFlush:
            if xNumber[4] != yNumber[4]:
                return xNumber[4] > yNumber[4]
            elif xNumber[3] != yNumber[3]:
                return xNumber[3] > yNumber[3]
            elif xNumber[2] != yNumber[2]:
                return xNumber[2] > yNumber[2]
            elif xNumber[1] != yNumber[1]:
                return xNumber[1] > yNumber[1]
            elif xNumber[0] != yNumber[0]:
                return xNumber[0] > yNumber[0]
        else:
            return True
    elif yFlush:
        return False

    if xStraight:
        if yStraight:
            return xNumber[4] > yNumber[4]
        else:
            return True
    elif yStraight:
        return False

    if xhasTriple:
        if yhasTriple:
            return xTriples[0] > yTriples[0]
        else:
            return True
    elif yhasTriple:
        return False

    if len(xDouble) == 2:
        if len(yDouble) == 2:
            if xDouble[1] != yDouble[1]:
                return xDouble[1] > yDouble[1]
            elif xDouble[0] != yDouble[0]:
                return xDouble[0] > yDouble[0]
            elif xNumber[4] != yNumber[4]:
                return xNumber[4] > yNumber[4]
            elif xNumber[3] != yNumber[3]:
                return xNumber[3] > yNumber[3]
            elif xNumber[2] != yNumber[2]:
                return xNumber[2] > yNumber[2]
            elif xNumber[1] != yNumber[1]:
                return xNumber[1] > yNumber[1]
            elif xNumber[0] != yNumber[0]:
                return xNumber[0] > yNumber[0]
        else:
            return True
    if len(yDouble) == 2:
        return False

    if xhasDouble:
        if yhasDouble:
            if xDouble[0] != yDouble[0]:
                return xDouble[0] > yDouble[0]
            elif xNumber[4] != yNumber[4]:
                return xNumber[4] > yNumber[4]
            elif xNumber[3] != yNumber[3]:
                return xNumber[3] > yNumber[3]
            elif xNumber[2] != yNumber[2]:
                return xNumber[2] > yNumber[2]
            elif xNumber[1] != yNumber[1]:
                return xNumber[1] > yNumber[1]
            elif xNumber[0] != yNumber[0]:
                return xNumber[0] > yNumber[0]
        else:
            return True
    if yhasDouble:
        return False

    if xNumber[4] != yNumber[4]:
        return xNumber[4] > yNumber[4]
    elif xNumber[3] != yNumber[3]:
        return xNumber[3] > yNumber[3]
    elif xNumber[2] != yNumber[2]:
        return xNumber[2] > yNumber[2]
    elif xNumber[1] != yNumber[1]:
        return xNumber[1] > yNumber[1]
    return xNumber[0] > yNumber[0]

for line in file:
    line = line.strip()
    tokens = line.split(" ")
    x = tokens[:5]
    y = tokens[5:]
    if player1Won(x,y):
        counter += 1

print(counter)
input("Done")
            


    
    






        

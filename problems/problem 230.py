print("Starting")

import useful, math

A= 1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
B= 8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196

AList = useful.intToList(A)
BList = useful.intToList(B)

Fn = [] ## [1,1,2,3,5,...]
for n in range(1,75): ##did some studies, need to go up to 75 and no more.
    Fn.append(useful.Feb(n)) ##not the most efficient way, but fuck it


answer = 0

def getLetter(i,pos):
    if i == 2 and pos == 1:
        return 'A'
    if i == 2 and pos == 2:
        return 'B'
    if i == 1:
        return 'B'
    if pos>Fn[i-2]:
        return getLetter(i-1,pos-Fn[i-2])
    else:
        return getLetter(i-2,pos)

def h(n):
    g =(127+19*n)*7**n
    temp = g/100
    for i in range(len(Fn)):
        if Fn[i] >temp:
            #letter = Fab[i][math.floor(temp)]
            temp2 = g - 100*math.floor(temp)
            pos = math.ceil(temp)
            letter = getLetter(i,pos)
            print(letter)
            if letter == 'A':
                return AList[temp2-1]
            else:
                return BList[temp2-1]

for n in range(18):
    answer+=10**n*h(n)

print(answer)

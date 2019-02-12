print("Starting")

import math, random

boardPlaces = []

for i in range(0,40):
    boardPlaces.append(0)

def roll():
    number = 4*random.random()
    number = math.ceil(number)
    number2 = 4*random.random()
    number2 = math.ceil(number2)
    total = number + number2
    return [total, number == number2]

def CC(x):
    number = 16*random.random()
    number = math.ceil(number)
    if number == 1:
        return 0
    if number == 2:
        return 10
    return x

def CH(x):
    number = 16*random.random()
    number = math.ceil(number)
    if number == 1:
        return 0
    if number == 2:
        return 10
    if number == 3:
        return 11
    if number == 4:
        return 24
    if number == 5:
        return 39
    if number == 6:
        return 5
    if number == 7 or number == 8:
        if x>35 or x<5:
            return 5
        if x>5 and x<15:
            return 15
        if x>15 and x<25:
            return 25
    if number == 9:
        if x<12 or x>28:
            return 12
        if x>12 and x<28:
            return 28
    if number == 10:
        return x-3
    return x

currentLocation = 0

for i in range(0,1000000):
    rollValue = roll()
    currentLocation += rollValue[0]
    currentLocation %= 40
    if currentLocation == 30:
        currentLocation = 10
    elif currentLocation == 2 or currentLocation == 17 or currentLocation == 33:
        currentLocation = CC(currentLocation)
    elif currentLocation == 7 or currentLocation == 22 or currentLocation == 36:
        currentLocation = CH(currentLocation)
    boardPlaces[currentLocation]+=1
    if rollValue[1]:
        rollValue = roll()
        currentLocation += rollValue[0]
        currentLocation %= 40
        if currentLocation == 30:
            currentLocation = 10
        elif currentLocation == 2 or currentLocation == 17 or currentLocation == 33:
            currentLocation = CC(currentLocation)
        elif currentLocation == 7 or currentLocation == 22 or currentLocation == 36:
            currentLocation = CH(currentLocation)
        boardPlaces[currentLocation]+=1
        if rollValue[1]:
            rollValue = roll()
            if rollValue[1]:
                currentLocation = 10
            else:
                currentLocation += rollValue[0]
                currentLocation %= 40
                if currentLocation == 30:
                    currentLocation = 10
                elif currentLocation == 2 or currentLocation == 17 or currentLocation == 33:
                    currentLocation = CC(currentLocation)
                elif currentLocation == 7 or currentLocation == 22 or currentLocation == 36:
                    currentLocation = CH(currentLocation)
                boardPlaces[currentLocation]+=1

best = 0
bestI = -1
secondBest = 0
secondBestI = -1
thirdBest = 0
thirdBestI = -1

for i in range(0,40):
    if boardPlaces[i] > best:
        thirdBest = secondBest
        thirdBestI = secondBestI
        secondBest = best
        secondBestI = bestI
        best = boardPlaces[i]
        bestI = i
    if boardPlaces[i] < best and boardPlaces[i] > secondBest:
        thirdBest = secondBest
        thirdBestI = secondBestI
        secondBest = boardPlaces[i]
        secondBestI = i
    if boardPlaces[i] < secondBest and boardPlaces[i] > thirdBest:
        thirdBest = boardPlaces[i]
        thirdBestI = i    
   
print(bestI,secondBestI,thirdBestI)
input("Done")   











    

    
    

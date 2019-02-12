## answer should be 4640261571849533
##
##4640261571849533

from random import *

def crossover(a,b):
    a=str(a)
    b=str(b)
    cut = randrange(digitLen)
    return int(a[:cut]+b[cut:])

def mutation(a):
    a=str(a)
    while len(a) < digitLen:
        a='0'+a
    aList = []
    for d in a:
        aList.append(d)
    for j in range(randrange(digitLen)):
        randindex = randrange(digitLen)
        aList[randindex] = str(randrange(10))
    return int(''.join(aList))

def exchange(a):
    a=str(a)
    while len(a) < digitLen:
        a = '0' + a
    aList = []
    for d in a:
        aList.append(d)
    randindex1 = randrange(digitLen)
    randindex2 = randrange(digitLen)
    aList[randindex1], aList[randindex2] = aList[randindex2], aList[randindex1]
    return int(''.join(aList))

def fitness(n):
    n=str(n)
    while len(n)<digitLen:
        n='0'+n
    fitLevel = 0
    for rule in guessList:
        correct = 0
        test = str(rule[0])
        while len(test)<digitLen:
            test='0'+test
        for i in range(digitLen):
            if test[i] == n[i]:
                correct += 1
        if correct == rule[1]:
            fitLevel += 1
    return ruleLen - fitLevel

def rouletteWheel(parents, total):
    if total == 0:
        return choice(parents)
    val = randrange(total)
    for p in parents:
        val -= (ruleLen - p[0])
        if val <=0:
            return p
    return

guessesTest = [(90342, 2), (70794, 0), (39458, 2), (34109, 1), (51545, 2), (12531, 1)]
guesses = [(5616185650518293, 2), (3847439647293047, 1), (5855462940810587, 3), (9742855507068353, 3), (4296849643607543, 3), (3174248439465858, 1), (4513559094146117, 2), (7890971548908067, 3), (8157356344118483, 1), (2615250744386899, 2), (8690095851526254, 3), (6375711915077050, 1), (6913859173121360, 1), (6442889055042768, 2), (2321386104303845, 0), (2326509471271448, 2), (5251583379644322, 2), (1748270476758276, 3), (4895722652190306, 1), (3041631117224635, 3), (1841236454324589, 3), (2659862637316867, 2)]

guessList = guesses
##tempIn = input().split('\n')[1:]
##guessList = []
##for s in tempIn:
##    p = s.split()
##    guessList.append((int(p[0]), int(p[1])))
digitLen = len(str(guessList[0][0]))
ruleLen = len(guessList)
totalRight = sum(x[1] for x in guessList)
parentSize = 100
childPerGen = 1000
reset = 2000

mutationRate = 50
exchangeRate = 50

parent = [(ruleLen-1, randrange(10**digitLen)) for i in range(parentSize)]
z = 0
while True:
    z +=1
    if z%reset == 0:
        parent = [(ruleLen, randrange(10**digitLen)) for i in range(parentSize)]
    print(z,parent[0], parent[-1])
    child = []
    total = sum(ruleLen - x[0] for x in parent)
    for k in range(childPerGen):
        tempP1 = rouletteWheel(parent,total)[1]
        tempP2 = rouletteWheel(parent,total)[1]
        child1 = crossover(tempP1, tempP2)
        if randrange(100) < mutationRate:           
            child1 = mutation(child1)

        if randrange(100) < exchangeRate:           
            child1 = exchange(child1)

        fitness1 = fitness(child1)
        child.append((fitness1,child1))

    child = sorted(list(child))
    if child[0][0] == 0:
        print(child[0][1])
        break
    else:
        parent = child[:50]
        totalc = sum(ruleLen - x[0] for x in child)
        while len(parent) < parentSize:
            temp = rouletteWheel(child,totalc)
            if temp not in parent:
                parent.append(temp)

        

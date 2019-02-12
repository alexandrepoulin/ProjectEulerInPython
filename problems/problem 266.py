import useful
from random import *

primes = useful.primesTo(190)
primes.sort()
sqrtProd = 1
for p in primes:
    sqrtProd*=p**(0.5)

length = len(primes)

def crossover(a,b):
    cut = randrange(length)
    return a[:cut]+b[cut:]

def mutations(a):
    num = randrange(length)
    a[num] = not a[num]
    return a

def exchange(a):
    num1 = randrange(length)
    num2 = randrange(length)
    while num2 == num1:
        num2 = randrange(length)
    temp = a[num1]
    a[num1] = a[num2]
    a[num2] = temp
    return a

def toNum(a):
    val = 1
    for i in range(length):
        if a[i]:
            val*=primes[i]
    return val

def fitness(a):
    val = toNum(a)
    if val > sqrtProd:
        return -1
    return sqrtProd-val

##answer 2323218950659046189161096883702440585

parentSize = 100
childPerGen = 1000

mutationRate = 20
exchangeRate = 20
newGenesRate = 5

reset = 2000

#temp = [[False]*length for i in range(length)]
#for i in range(length):
#    temp[i][i] = True
#temp = temp + [[True]*25+[False]*(length-25)]
#temp = temp + [[False]*(length-16)+[True]*(16)]
#1.372104556578805e+30
#temp = temp + [[False, True, False, False, False, True, True, False, False, False, False, True, False, False, True, True, False, True, True, False, True, True, False, True, False, True, False, True, False, True, False, False, False, True, True, True, True, False, True, False, False, True]]
#temp = temp + [[False, False, True, True, False, False, False, True, False, False, False, False, True, True, False, True, True, True, False, False, False, True, True, True, False, False, True, True, False, False, True, True, True, False, False, True, True, False, True, False, True, False]]
tempParents = []#temp
while len(tempParents)<parentSize:
    tempp = [False]*length
    for i in range(20):
        val = randrange(length)
        tempp[val] = True
    if fitness(tempp) != -1:
        tempParents = tempParents + [tempp]

parent = [[fitness(x), x] for x in tempParents]
parent.sort()
z=0

while True:
    z+=1
    parent.sort()
    print(z,parent[0][0],toNum(parent[0][1])%10**16)
    if parent[0][1] == 2323218950659046189161096883702440585:
        break 
    child = parent[:3]
    while len(child) < childPerGen :
        child1 = []
        if randrange(100)< newGenesRate:
            child1 =[False]*length
            for i in range(25):
                val = randrange(length)
                child1[val] = True
        else:
            randparent1 = choice(parent)[1]
            randparent2 = choice(parent)[1]
            while randparent2 == randparent1:
                randparent2 = choice(parent)[1]
            child1 = crossover(randparent1,randparent2)
            if randrange(100)< mutationRate:
                child1 = mutations(child1)
            if randrange(100)< mutationRate:
                child1 = mutations(child1)
            if randrange(100)< exchangeRate:
                child1 = exchange(child1)
            if randrange(100)< exchangeRate:
                child1 = exchange(child1)
        if len(child1) != length:
            continue
        fit = fitness(child1)
        if fit == -1:
            continue
        if [fit,child1] not in child:
            child.append([fit,child1])
    child.sort()
    parent=child[:5]
    while len(parent) < parentSize:
        temp = choice(child[5:])
        if temp not in parent:
            parent.append(temp)


print("Starting")

import useful

##the positions will start at the top right, go closewise and the last one is the middle

tiles0 = [True,True,True,True,True,True,False]
tiles1 = [True,True,False,False,False,False,False]
tiles2 = [True,False,True,True,False,True,True]
tiles3 = [True,True,True,False,False,True,True]
tiles4 = [True,True,False,False,True,False,True]
tiles5 = [False,True,True,False,True,True,True]
tiles6 = [False,True,True,True,True,True,True]
tiles7 = [True,True,False,False,True,True,False]
tiles8 = [True,True,True,True,True,True,True]
tiles9 = [True,True,True,False,True,True,True]
tilesBLANK = [False,False,False,False,False,False,False]
numbers = [tiles0,tiles1,tiles2,tiles3,tiles4,tiles5,tiles6,tiles7,tiles8,tiles9,tilesBLANK]

transitions = [] ##for MAX's clock, counts how many transitions
for i in range(len(numbers)):
    transLine = []
    currentInitial = numbers[i] ## if I is 10, then it is blank
    for j in range(len(numbers)):
        finalNumber = numbers[j]
        val = 0
        for k in range(7):
            if (currentInitial[k] and not finalNumber[k]) or (not currentInitial[k] and finalNumber[k]):
                val += 1 ## this take the case where need to turn a cell on, or off
        
        transLine.append(val)
    transitions.append(transLine)
##I'll pass in -1 for a the initial turn on or the final turn off
def numberOfTforMax(initial,final):
    answer = 0
    initialList = []
    finalList = []
    if initial != -1 and final != -1:
        initialList = useful.intToList(initial)
        finalList = useful.intToList(final)    
    if initial == -1:
        finalList = useful.intToList(final)
        initialList=[10]*len(finalList)
    if final == -1:
        initialList = useful.intToList(initial)
    for i in range(len(initialList)):
        if i< (len(initialList) - len(finalList)):
            answer += transitions[initialList[i]][10] ##for a blank
        else:
            answer += transitions[initialList[i]][finalList[i-len(initialList)]] ##for a blank
    return answer


temp=10**7
primes = useful.primesTo(2*temp)
primes = [p for p in filter(lambda k: k>temp, primes)]
primes.sort()
leng = len(primes)
samTrans = 0
maxTrans = 0

for i in range(len(primes)):
    if (i%1000) == 0:
        print(i, "of ", leng)
    p = primes[i]
    current = -1
    nextVal = p
    while current != nextVal:
        maxTrans += numberOfTforMax(current,nextVal)
        samTrans += 2*numberOfTforMax(-1,nextVal)
        current = nextVal
        nextVal = useful.addDigits(current)
    maxTrans += numberOfTforMax(current,-1)

print(samTrans,maxTrans)
print(samTrans-maxTrans)
input("Done")

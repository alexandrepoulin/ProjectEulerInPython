print("Starting")

import useful

def nextNum(x):
    fact = useful.factors(x)
    return sum(fact)+1
MAX = 1000000
bestLength = 0
bestNum = 0
bestChain = []
numbers = set(range(MAX,2,-1))
while numbers:
    print(len(numbers))
    i = numbers.pop()
    nextNumber = nextNum(i)
    currenChain = [i]
    found = True
    while nextNumber != i:
        if nextNumber == 1:
            found = False
            break
        if nextNumber == currenChain[0]:
            break
        if nextNumber >= MAX:
            found = False
            break
        if nextNumber in currenChain:
            index = currenChain.index(nextNumber)
            currenChain = currenChain[index:]
            break
        currenChain.append(nextNumber)
        nextNumber = nextNum(nextNumber)
    if found:
        val = len(currenChain)
        if val > bestLength:
            bestNum = min(currenChain)
            bestLength = val
            bestChain = currenChain
    numbers.difference_update(set(currenChain))
print(bestChain)
print(bestLength)
print(bestNum)
input("Done")

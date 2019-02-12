print("Starting...")

chainCounter = 1
longestSoFar = 0
currentNumInChain = 0
bestNumberSoFar = 0

def function(num):
    if num%2 == 0:
        return num/2
    return 3*num+1

for i in range(1000000):
    chainCounter = 1
    currentNumInChain = i
    while currentNumInChain > 1:
        currentNumInChain = function(currentNumInChain)
        chainCounter+=1
    if chainCounter>longestSoFar:
        longestSoFar=chainCounter
        bestNumberSoFar = i
    if i%1000 == 0:
        print(i)

print(bestNumberSoFar)

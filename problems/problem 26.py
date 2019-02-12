print("Starting")

from mpmath import *

mp.dps = 4000
sigfigs = 4000

def getNum(d):
    x= fdiv(1,d)
    return nstr(x,n=sigfigs)

def answer(a):
    currentBestLength = 0
    currentBestInt = 0
    for d in range(2,a):
        x = getNum(d)
        if len(x) < 90:
            continue
        num = getNum(d)[30:]
        currentChain = num[0]
        length = 1
        while True:
            print(d)
            if num[length:2*length] == currentChain and num[2*length:3*length] == currentChain:
                if length > currentBestLength:
                    currentBestLength = length
                    currentBestInt = d
                break
            else:   
                currentChain = num[:length+1]
                length+=1
        print(currentBestLength)
    return currentBestInt

#print(getNum(977))
print(answer(1000))

input("Press something to close")

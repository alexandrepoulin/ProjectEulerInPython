print("starting")

sumOfPals = 0

def inBinary(x):
    largestPower = 0
    binaryText = ""
    currentNum=x
    while x>=2**(largestPower+1):
        largestPower +=1
    for i in range(largestPower,-1,-1):
        if 2**i<=currentNum:
            binaryText += "1"
            currentNum -=2**i
        else:
            binaryText += "0"
    return binaryText

def isPal(x):
    l = len(x)-1
    for i in range(0,len(x)):
        if i >= l-i:
            break
        if x[i] != x[l-i]:
            return False
    return True

for i in range(1,1000001,2):
    print(i)
    if isPal(str(i)) and isPal(inBinary(i)):
        sumOfPals += i

print(sumOfPals)

input("press Something")

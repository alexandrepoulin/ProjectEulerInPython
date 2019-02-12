print("starting")

MAX = 10000000000

sumOfValues = 0

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

def findValue(x):
    binary = inBinary(x)
    powers = [x]
    product = 1
    for i in range(0,len(binary)-1):
        powers.append(powers[i]**2 % MAX)
    for i in range(0,len(binary)):
        if binary[i] == "1":
            product = (product*powers[len(binary)-i-1] % MAX)
    return product
    

for i in range(1,1001):
    sumOfValues = (sumOfValues+findValue(i))% MAX

print(sumOfValues)
    
    

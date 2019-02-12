print("Starting...")

def sumOfDivisors(x):
    sumSoFar = 0
    for i in range(1,int(x/2)+1):
        if x%i == 0 :
            sumSoFar+=i
    return sumSoFar

def findAmicableUpTo(x):
    isAmicable = []
    for i in range(1,x):
        if i == sumOfDivisors(sumOfDivisors(i)) and i != sumOfDivisors(i) and set(isAmicable).isdisjoint([i]):
            isAmicable.append(i)
            if sumOfDivisors(i) < x:
                isAmicable.append(sumOfDivisors(i))
    return isAmicable
        
def summing(x):
    sumSoFar = 0
    for i in range(0,len(x)):
        sumSoFar += x[i]
    return sumSoFar


print(summing(findAmicableUpTo(10000)))




























print("Done")

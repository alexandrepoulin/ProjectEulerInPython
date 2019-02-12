import math

maxVal =10**15
maxValSqrt = math.floor(maxVal**0.5)
mod=10**9


def generateKList(m):
    return [math.floor(maxVal/(m+1))+1 , math.floor(maxVal/m)]

def S(m,n):
    if n==1:
        return m*(m+1)*(2*m+1)//6
    return S(m,1) - S(n-1,1)


print(maxValSqrt)

answer = 0

for i in range(1,maxValSqrt+1):
    if i%1000000==0:
        print(i)
    answer += i**2 * (maxVal//i)
    answer %= mod
    kList = generateKList(i)
    answer += S(kList[1],kList[0])* i
    answer %= mod


print(answer)

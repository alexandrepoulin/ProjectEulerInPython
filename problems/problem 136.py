import math

nMax = 100

def getMax(aVal):
    return math.floor(1/3*(math.sqrt(4*aVal**2+3*nMax)-aVal))

def calc(a,d):
    return 3*d**2+2*d*a-a**2

answer = 0
for a in range(1,math.ceil((nMax-3)/4)+1):
##    if a%100000 == 0:
##        print(a,answer)
    dmax = min([math.floor(a/2),getMax(a)])
    dmin = math.ceil(a/3)
    if dmax <dmin:
        continue
  
    answer += dmax-dmin

print(answer)

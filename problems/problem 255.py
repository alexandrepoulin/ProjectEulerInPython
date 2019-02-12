print("Starting")

import math

x0 = 7*10**6

def start(N,xk):
    currentX = 0
    nextX=xk
    xs= [xk]
    while currentX != nextX:
        currentX=nextX
        nextX = math.floor(0.5*(currentX+math.ceil(N/nextX)))
        if currentX != nextX:
            xs.append(nextX)
    return xs

def itterate(N,xk):
    return math.floor(0.5*(xk+math.ceil(N/xk)))

x = []
MinVal = 10**13
MaxVal = 10**14
limits = [MaxVal]

answer = 0
currentNum = MinVal
progress = 0
while len(limits)>0:
    if currentNum - progress > 10**10:
        progress = currentNum
        print(progress)
    x = start(currentNum,x0)
    for s in x:
        l = (math.ceil(currentNum/s))*s+1
        if limits[-1] > l:
            limits.append(l)
    answer += (limits[-1]-currentNum)*len(x)
    currentNum = limits[-1]
    del limits[-1]

print("the answer is",answer/(MaxVal-MinVal))
input("Done")
    
    
    



print("starting")

import math

##the equation we want to solved is x^2-x-k where x=2^t
## a solution occurs when sqrt(1+4*k) is an integer
## a perfect solution occures when log_2(1+sqrt(1+4*k)) is an integer

##Solving N^2-4k-1=0 gives the values of k for which an integer exist
## these solutions are given by:
## N=4u+1
## k=4u^2+2u
## and
## N= 4u+3
## k= 4u^2 +6u+2


perfect = 0
total = 0
answer = []
k = 0
val = 1/12345.0
u1 = 1
u2 = 0

def next(u,v):
    temp1 = 4*u**2+2*u
    temp2 = 4*v**2+6*v+2
    if temp1 < temp2:
        return [u+1,v,4*u+1, temp1]
    return [u,v+1,4*v+3,temp2]

while True:
    temp = next(u1,u2)
    u1 = temp[0]
    u2= temp[1]
    total +=1
    temp2 = math.log(1+temp[2],2)
    if int(temp2) == temp2:
        perfect += 1
    if total !=0:
        temp3 =(perfect/total)
        if(total%10000 == 0):
            print(total,temp3)
        if temp3<val:
            answer = temp
            break

print(answer)

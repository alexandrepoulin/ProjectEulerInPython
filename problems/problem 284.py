print("Starting")

import math

def countDigits(x,newB):
    temp = math.floor(math.log(x,newB))+1
    answer = x%newB
    for i in range(temp,1,-1):
        answer += ((x%newB**i)-(x%newB**(i-1)))/newB**(i-1)
    return int(answer)

def changeB(x,newB):
    answer = ""
    temp = math.floor(math.log(x,newB))+1
    for i in range(temp,0,-1):
        val = x%newB
        if i != 1:
            val = ((x%newB**i)-(x%newB**(i-1)))/newB**(i-1)
        if val <10:
            answer += str(int(val))
        elif val == 10:
            answer += "a"
        elif val == 11:
            answer += "b"
        elif val == 12:
            answer += "c"
        elif val == 13:
            answer += "d"
    return answer


base = 14
n = 10000
answer = 0

vals = []
for m in range(1,n+1):
    if m%100 == 0:
        print(m)
    nVals = []
    for j in range(0,base):
        if m != 1:
            for k in vals[m-2]:
                temp = j*base**(m-1)+k
                if (temp)**2%(base**m) == (temp):
                    nVals.append(temp)
                    if j!=0:
                        answer += countDigits(temp,base)
        else:
            temp = j
            if j**2%(base) == (j):
                nVals.append(j)
                if j!=0:
                    answer += countDigits(temp,base)
    vals.append(nVals)

print(answer)
print(changeB(answer,base))

##604557993
##5a411d7b
##>>> print(len(vals))
##10000
##>>> print(len(vals[-1]))
##4
##>>> x = sum(len(y) for y in vals)
##>>> print(x)
##40000
##>>> print(len(vals[0]))
##4
##>>> print(vals[0])
##[0, 1, 7, 8]
##>>> print(vals[1])
##[0, 1, 49, 148]
##>>> print(vals[2])
##[0, 1, 344, 2401]
##>>> print(vals[3])
##[0, 1, 2401, 36016]

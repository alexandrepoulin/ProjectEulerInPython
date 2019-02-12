print("Starting")

import useful

digits = 10

MAX = int(10**(digits*0.5))

primes = useful.primesTo(MAX)

def increase(perm,current,d):
    changed = False
    maxNum = 9
    minNum = 0
    answer = current
    if d == 9:
        maxNum = 8
    if d == 0:
        minNum = 1
    for i in range(0,digits):
        if perm[digits-1-i] == 1:
            continue
        if useful.getDigit(i+1,current) == maxNum:
            continue
        if useful.getDigit(i+1,current) == d-1:
            answer = useful.incDigit(i+1,current,2)
            for j in range(0,i):
                if perm[digits-1-j] == 1:
                    continue
                answer = useful.setDigit(j+1,answer,minNum)
            changed = True
            break
        answer = useful.incDigit(i+1,current,1)
        for j in range(0,i):
            if perm[digits-1-j] == 1:
                continue
            answer = useful.setDigit(j+1,answer,minNum)
        changed = True
        break
    if not changed:
        return 0
    return answer

def getInitial(perm,d):
    answer = 0
    for i in range(0,digits):
        answer += d*perm[digits-1-i]*10**i
    if perm[0] == 0:
        answer +=10**(digits-1)
    return answer

## will return [M,N,S]
def s(d):
    for n in range(digits-1,0,-1):
        S = 0
        M = n
        N = 0
        perm = []
        for i in range(0,n):
            perm.append(1)
        for i in range(n,digits):
            perm.append(0)
        perm = useful.perm(perm)
        if d == 0:
            perm = [y for y in filter(lambda k: k[0] == 0, perm)]
        for p in perm:
            num = getInitial(p,d)
            while num != 0:
                if useful.fastIsPrime(num,primes,MAX):
                    S += num
                    N +=1
                num = increase(p,num,d)
        if N != 0:
            return [M,N,S]
    return -1

answer = 0
for k in range(0,10):
    temp = s(k)
    print(k,temp)
    answer += temp[2]
print(answer)

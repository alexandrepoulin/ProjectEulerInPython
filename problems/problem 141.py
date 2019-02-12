print("Starting")

import useful, math

maxNum = 10**12
##maxNum = 100000

## need special implementdation
def factFromMult(fact1,fact2,n):
    factors = set()
    for i in fact1:
        for j in fact2:
            temp = i*j
            if temp < n:
                factors.add(i*j)
    return factors ##this is a set

answer = 0
for n in range(1,int(maxNum**0.5)):
    if n%1000 == 0:
        print(n)
    temp = n**2
    factors = useful.factors(n)
    factors.append(1)
    factors.append(n)
    factors = factFromMult(factors,factors,n)
    for a in factors:
        #d = 0.5*(math.sqrt(a**4+4*a*temp)-a**2)
        d = round(math.pow((a*(temp-a)),(1/3)))
##        if abs(round(d)-d)>0.01:
##            continue
        #q = 0.5*(a**3+2*temp-a*math.sqrt(a**4+4*a*temp))
        q = round(a*math.pow(((temp-a)/a**2),(2/3)))
##        if abs(round(q)-q)>0.01:
##            continue
        if d*q+a == temp and d**2/a == q:
            answer += temp
            print(n,temp,d,q,a)
            break

                

print(answer)

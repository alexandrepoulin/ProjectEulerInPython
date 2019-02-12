print("Starting")

import useful

print("Making Factor list")

MAX = 2*10**7

print("Computing")
used = set()
answer = 0
for i in range(2,MAX+1):
    if i%1000 == 0:
        print(i,len(used))
    sFactor = useful.factFromMult(useful.factors(i-1),useful.factors(i+1))
    #sFactor = set(useful.factors(i**2-1))  
    sFactor.difference_update(used)    
    sFactor = [x for x in filter(lambda k: k > i and k <= MAX, sFactor)]
    for k in sFactor:
        answer = ((i)*(k-1))%k
        used.add(k)

print(answer)

input("Done")


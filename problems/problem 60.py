print("Starting")

import useful
from useful import fastIsPrime as pr
MAX = 10000
NUMBEROFPRIMES = 5
primes1 = useful.primesTo(MAX)
primes1.sort()
bestValues = []
found = False

for i in primes1:
    print(i)
    if i == 2 or i == 5:
        continue
    for j in primes1:
        if j < i:
            continue
        if pr(int(str(i)+str(j)),primes1,MAX) and pr(int(str(j)+str(i)),primes1,MAX):     
            for k in primes1:
                if k < j:
                    continue
                if pr(int(str(i)+str(k)),primes1,MAX) and pr(int(str(k)+str(i)),primes1,MAX) and pr(int(str(j)+str(k)),primes1,MAX) and pr(int(str(k)+str(j)),primes1,MAX):
                    for l in primes1:
                        if l < k:
                            continue
                        if pr(int(str(i)+str(l)),primes1,MAX) and pr(int(str(l)+str(i)),primes1,MAX) and pr(int(str(j)+str(l)),primes1,MAX) and pr(int(str(l)+str(j)),primes1,MAX) and pr(int(str(l)+str(k)),primes1,MAX) and pr(int(str(k)+str(l)),primes1,MAX):
                            for m in primes1:
                                if m < l:
                                    continue
                                if pr(int(str(i)+str(m)),primes1,MAX) and pr(int(str(i)+str(m)),primes1,MAX) and pr(int(str(j)+str(m)),primes1,MAX) and pr(int(str(m)+str(j)),primes1,MAX) and pr(int(str(m)+str(k)),primes1,MAX) and pr(int(str(k)+str(m)),primes1,MAX) and pr(int(str(m)+str(l)),primes1,MAX) and pr(int(str(l)+str(m)),primes1,MAX):
                                    smallestSum = i+j+k+l+m
                                    bestValues = [i,j,k,l,m]
                                    found = True
                                    break
                        if found:
                            break
                if found:
                    break
        if found:
            break
    if found:
        break
                            

print("The smallest sum is")
print(smallestSum)
print(bestValues)
input("Done")



            

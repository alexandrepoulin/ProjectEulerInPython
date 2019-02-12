print("Starting")

import useful

N = 20000000
K = 15000000

a= min(K,N-K)
b = max(K+1,N-K+1)
c=N

primes = useful.primesTo(c)
primes.sort()
nom = list(range(b,c+1))
denom = list(range(2,a+1))

denomSum = 0
nomSum = 0


for i in range(len(nom)):
    if (i%1000)==0:
        print(i)
    nomSum += sum(useful.factorsFromPrimes(nom[i],primes))

for i in range(len(denom)):
    if (i%1000)==0:
        print(i)
    denomSum += sum(useful.factorsFromPrimes(denom[i],primes))

print(nomSum-denomSum)
input("Done")

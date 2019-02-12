print("Starting")

##1/x+1/y=1/n => ny+nx-xy=0
## x(n-y)+ny=0 let y' = -y+n => y=n-y' => xy'+n^2-ny'=0
## y'(x-n)+n^2 = 0 let x'=x-n => x'y'+n^2 = 0
## as x,y>0 , we need either (x<n AND y<n) or (x>n AND y>n)
## can't have (x<n AND y<n) so we must have (x>n AND y>n)

## if n is prime => only solution is x'= n = -y' and -x'=n=y' => x=0 or 2n and y = 2n or 0
## if n is a product of primes p_i, assume that y' is neg and let y'' = -y':

## x'y''= n^2 =(p_1^r_1*p_2^r_2...*p_j^r_j)^2 
## the number of solutions will then be all possible combinations.

import useful
primes = useful.primesTo(10000)

counter = 3
solutions = 0
while solutions < 4*10**6:
    counter+=1
    factors = useful.factorsFromPrimes(counter,primes)
    uniqueFactors = set(factors)
    solutions = 1
    for f in uniqueFactors:
        sumOfComb = 2*factors.count(f)+1
        solutions *= sumOfComb
    solutions += 1
    solutions /= 2

print(counter)
input("Done")


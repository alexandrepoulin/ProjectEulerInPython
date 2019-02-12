print("Starting")

##for a number N, we want to find k such that (N/k)^k is a max
## d/dx (N/x)^x = (N/x)^x * (ln(N/x)-1), set equal to 0 gives
## x= N/e

##STRATEGY:
## for N, calculate x, test floor x and ceil x to see which is bigger, call it k
## if k=2^a*5^b, then it will terminate, so find the prime factors
import math
import useful

minNum = 5
maxNum = 10000
e = 2.718281828459045
primes = useful.primesTo(maxNum)

def getX(N):
    return N/e
def M(N,k):
    return k*math.log((N/k))
##using this instead of (N/k)**k because the numbers were too big

finalAnswer = 0
for N in range(minNum,maxNum+1):
    x = getX(N)
    k = 0
    if M(N,math.floor(x)) > M(N,math.ceil(x)):
        k = math.floor(x)
    else:
        k = math.ceil(x)
    g = useful.GCD(N,k)
    factors = set(useful.factorsFromPrimes(int(k/g),primes))
    factors.difference_update(set([2,5]))
    if len(factors) == 0 :
        finalAnswer -= N
    else:
        finalAnswer += N

print(finalAnswer)


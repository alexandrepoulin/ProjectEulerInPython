import useful as u
import math

mod = 1307674368000 
##primes = u.primesTo(15)
##facts = u.factorsFromPrimes(mod,primes)
##facts.sort()
##
##period = 1
##
##for p in primes:
##    fib = [1,1,2]
##
##    while fib[-2:] !=[1,1]:
##        fib.append((fib[-1]+fib[-2])%p)
##
##    per=len(fib)-2
##    period*=per*p**(facts.count(p)-1)


print(period)

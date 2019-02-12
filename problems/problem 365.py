import useful as u

primes = u.primesTo(5000)
primes = [x for x in filter(lambda k: k>1000,primes)]



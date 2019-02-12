print("Starting")

import useful

primes = useful.primesTo(1000003)
primes.sort()
primes = primes[2:]
answer = 0

for i in range(len(primes)-1):
    if i%1000 ==0:
        print(i)
    p1 = primes[i]
    p2 = primes[i+1]
    length = len(str(p1))
    sol = useful.euclidAlg(10**length,p2)
    answer += ((sol[1]*p1)%10**length)*p2

print(answer)
input("Done")

import useful as u

maxNum = 10**8
primes = u.primesTo(maxNum)
primes=primes[2:]
print(len(primes))
answer = 0
for c,p in enumerate(primes):
    if c%100000==0:
        print(c)
    q1 = u.euclidAlg(p-2,p)
    q2 = u.euclidAlg(p-3,p)
    q3 = u.euclidAlg(p-4,p)
    answer += (q1[0]*(1+q2[0]*(1+q3[0])))%p

print(answer)



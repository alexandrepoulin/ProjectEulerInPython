print("Starting")

import useful

primes = set(useful.primesTo(10000))
primes.difference_update(set(range(0,1001)))
primes = list(primes)
primes.sort()

answer = []

def fix(x):
    answer = ""
    for i in x:
        answer += i
    return answer

def fixAll(x):
    answer = []
    for i in x:
        answer.append(fix(i))
    return answer

for i in primes:
    print(i)
    for k in primes:
        if i >= k:
            continue
        if (2*k-i) in primes:
            x = fixAll(useful.perm(str(i)))
            if str(k) in x and str(2*k-i) in x:
                answer.append(str(i)+str(k)+str(2*k-i))

print(answer)

input("done")

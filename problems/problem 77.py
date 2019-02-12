print("Starting")

import useful, math

primes = useful.primesTo(5000)
primes.sort()

ways = [0]*5000
ways[0] = 1

for i in primes:
    for j in range(i, 5000):
        ways[j] += ways[j-i]
answer = 0
for i in range(0,5000):
    print(ways[i])
    if ways[i]>=5000:
        answer = i
        break

print(answer)   

            
        
        
    

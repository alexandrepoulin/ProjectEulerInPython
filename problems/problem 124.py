print("Starting")

import math
import useful

wantedK = 10000
MAX = 100000
numbers = set(range(MAX,1,-1))

#want E(10000)

counter = 1
notFound = True
answer = 0
while notFound:
    n = numbers.pop()
    factors = useful.primeFact(n)
    counters = [0]*len(factors)
    numbs = set()
    while True:
        val = n
        for i in range(0,len(factors)):
            val*=factors[i]**counters[i]
        if val > MAX:
            same = True
            for j in range(0,len(factors)):
                if counters[-j-1] != 0 and j+2 <= len(factors):
                    counters[-j-1] = 0
                    counters[-j-2] += 1
                    same = False
                    break
            if same:
                break
            continue
        counters[-1]+=1
        numbs.add(val)
    numbs.add(n)
    length = len(numbs)
    if counter + length < wantedK:
        counter+= length
        numbers.difference_update(numbs)
    else:
        numbs = list(numbs)
        numbs.sort()
        print(n)
        print(numbs)
        answer = numbs[wantedK-counter-1]
        notFound = False

print(answer)
input("Done")

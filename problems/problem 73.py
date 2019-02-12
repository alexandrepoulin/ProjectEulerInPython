print("Starting")

import fractions
import math
counter = 0
for q in range(4,12001):
    print(q)
    for p in range(math.ceil(q/3),math.ceil(q/2)):
        if fractions.gcd(q,p) == 1:
            counter+=1

print(counter)
input("Done")

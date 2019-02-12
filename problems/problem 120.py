print("Starting")

import math

sumSoFar = 0
for i in range(3,1001):
    if i % 2 == 1:
        sumSoFar += i*(i-1)
        continue
    sumSoFar += i*(i-2)

print(sumSoFar)
input("Done")
            

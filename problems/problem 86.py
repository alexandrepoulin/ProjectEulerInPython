print("Starting")

import math

numberOfSolutions = 0

MAX = 1

while numberOfSolutions < 10**6:
    MAX +=1
    print(numberOfSolutions)
    for b in range(1,MAX+1):
        for c in range(1,b+1):
            value = math.sqrt(MAX**2+(b+c)**2)
            if int(value) == value:
                numberOfSolutions+=1

print(MAX)
input("Done")

print("Starting")

import math

counter = 0
bestLine = 0

MAX = 0

file = open("base_exp.txt")

for line in file:
    counter += 1
    line = line.strip()
    tokens = line.split(",")
    value = math.log(int(tokens[0]))*int(tokens[1])
    if value > MAX:
        MAX = value
        bestLine = counter

print(bestLine)
input("Done")
        
    

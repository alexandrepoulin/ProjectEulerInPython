import useful
import random

print("Starting")

##fuck it, MC
turns = 1000000000
wins = 0
for i in range(turns):
    blue = 0
    for n in range(2,17):
        num = random.random()
        if num <= 1/n:
            blue+=1
    if blue >=8:
        wins+=1
answer = turns/wins
print(answer)


input("Done")
        

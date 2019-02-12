print("Starting")

def isPan(x):
    return set(str(x)) == set(str(123456789)) and len(str(x)) == 9

currentBest = 918273645
bestNum = 0

for i in range(9000, 10000):
    value = int(str(i)+str(2*i))
    if isPan(value) and value> currentBest:
        bestNum = i
        currentBest = value

print(currentBest)
print(bestNum)
input("done")
    

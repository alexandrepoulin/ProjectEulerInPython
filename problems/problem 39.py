print("Starting")

periCount = [[x,0] for x in range(0,1001)]

for a in range(1,1000):
    for b in range(1,1000):
        if b < a:
            c = (a**2+b**2)**0.5
            p = a+b+c
            if int(c) == c and p <= 1000:
                periCount[int(p)][1] +=1
            
bestSoFar = [0,0]

for x in periCount:
    if x[1] > bestSoFar[1]:
        bestSoFar = x

print(bestSoFar)
input("stuff")

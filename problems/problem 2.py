print("starting")

f1 = 1
f2 = 2

f3 = f1+f2

sumSoFar = 2

while f3 < 4000000:
    if f3%2 == 0:
        sumSoFar += f3
    temp = f2
    f2 = f3
    f3 += temp

print(sumSoFar)

input("Press something to finish")

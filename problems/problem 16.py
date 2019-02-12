print("Starting...")

theNumber = str(2**1000)
sum1 = 0

for i in range(len(theNumber)):
    sum1+= int(theNumber[i])

print(sum1)

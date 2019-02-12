print("Starting...")

a = 0
b = 0

import math

secbreak = False

for i in range(1, 1000):
    for k in range(1, 1000):
        if i+k+math.pow(i**2+k**2, 0.5) == 1000:
            a = i
            b = k
            secbreak = True
            break
    if secbreak:
        break

c = math.pow(a**2+b**2, 0.5)

print(a)
print(b)
print(c)
print(a*b*c)

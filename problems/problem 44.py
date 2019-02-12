print("Starting")

import math

def P(n):
    return n*(3*n-1)/2
def n(P):
    return (1+math.sqrt(1+24*P))/6

j = 1
found = False
answer = 0
while not found:
    print(j)
    for k in range(1,j):
        Pj = P(j)
        Pk = P(k)
        n1 = n(Pj-Pk)
        if int(n1) != n1:
            continue
        n2 = n(Pj+Pk)
        if int(n2) != n2:
            continue
        answer = Pj-Pk
        found = True
        break
    j+=1

print(answer)
input("Done")

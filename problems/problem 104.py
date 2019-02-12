print("Stating")

import useful
from mpmath import *

mp.dps = 100000
sigfigs = 100000

def cal(k):
    return 1/sqrt(5)*(((1+sqrt(5))/2)**k-((1-sqrt(5))/2)**k)

Fk = [0,1]
k = 1

notFound = True

while notFound:
    val = sum(Fk)%10**9
    Fk = [Fk[1],val]
    k+=1
    if k < 300000:
        continue
    print(k)
    if len(str(val))>=9:
        if useful.isPan(val):
            calVal = cal(k)
            string = str(calVal)[0:10]
            if '.' in string:
                string = string[0]+string[2:10]
            else:
                string = string[:9]
            notFound = not(useful.isPan(int(string)))

        

print(k)
input("Done")
        

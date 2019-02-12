print("Starting")

import fractions

MAX = 1500000
answer = [0]*MAX

for i in range(1, int(MAX**0.5+1),2):
    print(i)
    for j in range(2, int(MAX**0.5+1)-i,2):
        m = max(i,j)
        n = min(i,j)
        if fractions.gcd(n,m) == 1 and (m-n)%2 == 1 and 2*(m**2+n*m) <= MAX:
            val = 2*(m**2+m*n)
            for k in range(val,MAX,val):
                answer[k]+=1

print(answer.count(1))
input("Done")


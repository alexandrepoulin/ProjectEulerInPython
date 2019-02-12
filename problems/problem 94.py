print("Starting")

import fractions

MAX = 1000000000

answer = 0

for i in range(1, int(MAX**0.5/2+1),2):
    print(i)
    for j in range(2, int(MAX**0.5/2+1)-i,2):
        m = max(i,j)
        n = min(i,j)
        if fractions.gcd(n,m) == 1 and (m-n)%2 == 1:
            vals = [m**2-n**2,2*m*n,m**2+n**2]
            if abs(vals[2]-2*vals[1]) == 1:
                P1 = 2*(vals[2]+vals[1])
                if P1 < MAX:
                    answer += P1
            if abs(vals[2]-2*vals[0]) == 1:
                P2 = 2*(vals[2]+vals[0])
                if P2 < MAX:
                    answer += P2
                    
print(answer)
input("Done")


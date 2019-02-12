print("starting")
import math

##used lagrange multipliers, it gave x_i = i*x1
##using the condition, you get x1 = 2/(m+1) 

def findP(m):
    val = 1
    for n in range(1,m+1):
        base = 2*n/(m+1)
        val *= base**n
    return math.floor(val)

answer = 0
for i in range(2,16):
    answer += findP(i)
print(answer)

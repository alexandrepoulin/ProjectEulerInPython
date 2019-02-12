import math

mod = 10**9

a=(21**7)
b=(7**21)
c=(12**7)

N=math.floor(b/a-1)
aprime = (b-(N+1)*a)+1

answer =( a*(4*a-3*c)*(N+1)*N//2 + 4*a*(a-c)*(N+1)+aprime*(4*(a-c)+(N+1)*(4*a-3*c))+b*(b+1)//2 )%mod
print(answer)

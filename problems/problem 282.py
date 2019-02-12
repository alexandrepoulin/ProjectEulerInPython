print("Starting")
import useful
primes = useful.primesTo(10)

modding = 14**8

answer = 1 + (1+2) +(2*2+3)+(2**(3+3)-3) ## A(0,0)+A(1,1)+A(2,2)+A(3,3)

## general form, using u^k for k Knuths up arrows:
## A(n,y)=2(u^n)(y+3)-3

##it can be shown (see notebook where you worked this out on paper) that A(4,4)=A(5,5)=A(6,6) mod 14**8
## and that A(4,4)=(2**52488-3)mod 14**8=488146685
answer +=3*488146685
answer %= modding
print(answer)

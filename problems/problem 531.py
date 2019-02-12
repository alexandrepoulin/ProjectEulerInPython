import useful as u

maxNum = 1005000

primes = u.primesTo(maxNum)

phis = [u.phi(n, primes) for n in range(1000000,maxNum+1)]

def solve(a,n,b,m):
    ##an easy check based on even and odd numbers to immediately tell if its going to fail
    if n%2 == 0 and m%2 ==0:
        if (a%2==0 and b%2 !=0) or (a%2!=0 and b%2 ==0):
            return 0
    ##well this case is obvious
    if(a==b):
        return a
    ##check eq 1
    gcd = u.GCD(n,m)
    if (b-a)%gcd !=0:
        return 0
    
    c = n//gcd
    mod = m//gcd
    rhs = ((b-a)//gcd)%mod
    euclidAnswer = u.euclidAlg(c,mod)
    x = (a+n*euclidAnswer[0]*rhs)%(n*mod)

    return x


answer = 0
for n in range(1000000,maxNum-1):
    if n%100==0:
        print(phis[n%1000000],n)
    for m in range(n+1,maxNum):
        answer+=solve(phis[n%1000000],n,phis[m%1000000],m)

print(answer)

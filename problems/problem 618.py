import useful, math

fibMax = 24
fib=[1,1]
for i in range(2,fibMax) :
    fib.append(fib[-1]+fib[-2])
primes = useful.primesTo(fib[-1]+1)

## Let Ak be the set of number such that the factors add to k
## S(k)= Sum over Ak
## note that Ak= (Union Ai * Aj) over i,j such that i+j=k, and where multiplication
## means the set of products that one can make. We must also add k if k is prime

##The previous method was too slow because it repeated stuff like adding
##18 to A8 because 18=3*6 (from A3*A5) and 18=2*9 (from A2*A6), and
##this spiralled out of control. This approach avoids this
##define mat[j][k]=mat[j-1][k]+pj*mat[j][k-pj], with pj being the jth prime
##imagine just factoring out the biggest prime, and you get this relation
##also if k-pj=0, then that means that k is just the prime
##start with mat[0][k]=1, mat[j][0]=1, and then S(k)=mat[-1][k-1]

##in reality, we just need to store the last line


currentLine=[0]*(fib[-1]+1)

for p in primes:
    newLine =currentLine[:p]+[currentLine[p]+p];
    for k in range(p+1,fib[-1]+1):
        newLine.append((currentLine[k]+p*newLine[k-p])%(10**9))
    currentLine=newLine

print((sum([currentLine[f] for f in fib[2:]]))%(10**9))


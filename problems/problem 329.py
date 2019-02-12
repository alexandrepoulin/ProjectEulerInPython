import useful as u

def t(x,y):
    return (x[0]*y[0],x[1]*y[1])
def a(x,y):
    return (x[0]*y[1]+x[1]*y[0],x[1]*y[1])
def comb(x,y,z):
    return (x[0]*(y[0]*z[1]+z[0]*y[1]),2*x[1]*y[1]*z[1])


primes = u.primesTo(500)

probP = [0]
probN = [0]
for i in range(1,501):
    if i in primes:
        probP.append((2,3))
        probN.append((1,3))
    else:
        probP.append((1,3))
        probN.append((2,3))

##1 is P, 0 is N
sequence = [1,1,1,1,0,0,1,1,1,0,1,1,0,1,0]
sequence.reverse()
probSoFar =probN.copy()
for i in range(1,len(sequence)):

    newProb = [0]
    if sequence[i]==1:
        val =t(probSoFar[2],probP[1])
        gcdV = u.GCD(val[0],val[1])
        newProb.append((val[0]//gcdV,val[1]//gcdV))
        for i in range(2,500):
            val = comb(probP[i],probSoFar[i-1],probSoFar[i+1])
            gcdV = u.GCD(val[0],val[1])
            newProb.append((val[0]//gcdV,val[1]//gcdV))
        val = t(probSoFar[499],probP[500])
        gcdV = u.GCD(val[0],val[1])
        newProb.append((val[0]//gcdV,val[1]//gcdV))
    else:
        val =t(probSoFar[2],probN[1])
        gcdV = u.GCD(val[0],val[1])
        newProb.append((val[0]//gcdV,val[1]//gcdV))
        for i in range(2,500):
            val = comb(probN[i],probSoFar[i-1],probSoFar[i+1])
            gcdV = u.GCD(val[0],val[1])
            newProb.append((val[0]//gcdV,val[1]//gcdV))
        val = t(probSoFar[499],probN[500])
        gcdV = u.GCD(val[0],val[1])
        newProb.append((val[0]//gcdV,val[1]//gcdV))
    probSoFar = newProb.copy()

total = (0,1)
for p in probSoFar[1:]:
    total = a(total,p)
total = (total[0],500*total[1])
gcd = u.GCD(total[0],total[1])
total = (total[0]//gcd,total[1]//gcd)
print(str(total[0])+"/"+str(total[1]))


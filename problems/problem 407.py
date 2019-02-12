import useful as u

maxNum = 10**7

primes = u.primesTo(maxNum)

answer = 0 ##skipping 1 in the loop because its the only one to give 0

def M(n):
    factors = set(u.compressFactors(u.factorsFromPrimes(n,primes)))
    N = 1
    for f in factors:
        N*=f
    NiFact = []
    for f in factors:
        euclid = u.euclidAlg((N//f)%f,f)
        NiFact.append((N//f*euclid[0])%N)
    length = len(NiFact)
    results =set()
    for j in range(2**length):
        ind = u.baseConvert10NumList(j,2)
        res = 0
        for k,c in enumerate(ind):
            res += NiFact[k]*c
        res%=N
        results.add(res)
    maxVal = max(results)
##    if(maxVal**2)%n!=maxVal:
##        print(n,maxVal)
    return maxVal

for i in range(2,maxNum+1):
    if i%10**5==0:
        print(i)
    
    answer += M(i)

print(answer)
                        
    

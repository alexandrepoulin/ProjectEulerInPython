

p=61
q=10**7
bigModPow = 10
bigMod=p**bigModPow

def tnGen():
    s = 290797
    mod = 50515093
    while True:
        s*=s
        s%=mod
        yield s%p
        

gen = tnGen()


primeSum = [((p**(k+1)-1)//(p-1))%bigMod for k in range(bigModPow)]

answer = 0
for i in range(1,q+1):
    tn = next(gen)
    if i < bigModPow:
        answer+=tn*primeSum[i-1]
    else:
        answer+=tn*primeSum[-1]
    answer%=bigMod
print(answer)
    



    

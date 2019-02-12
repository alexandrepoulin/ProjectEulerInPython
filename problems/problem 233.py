import useful as u
import math

##Let r'_2(n) be the number of ways to write n as an unordered sum of 2 squares
##greater than 0.

##for n = 2^a_0 * p_1^(2a_1) * ... * p_k^(2a_k) * q_1^b_1 * ... * q_r^b_r
##where p=4k+3 and q=4k+1 are primes then defining:
##B=(b_1+1) * ... * (b_r+1)
##r'_2(n)=0 if a_i are half integers
##       = B/2 if B is even
##       = (B-(-1)^a_0)/2 if B is odd

##Since we care about r'_2(n^2), a_0 is always even, B is always odd, and a_i
##are never half integers. Furthermore, if we want the total number of solutions
##to be 420, then we want r'_2(n^2)+1=(420+4)/8 = 53, which gives B=105
## or B=3*5*7
##This means we need n=2^a_0 * p_1^a_1 ... p_k^a_k * q_1 * q_2^2 * q_3^3
##The smallest n possible is n=17*13^2*5^3 = 359125. This means we only need to
##find primes up to floor((10^11)/(13^2*5^3))
##we also only need to find p up to floor((10^11)/(17*13^2*5^3))


biggestN=10**11 
qMax = math.floor(biggestN/(13**2*5**3))+1
pMax = math.floor(biggestN/(17*13**2*5**3))+1


primes = u.primesTo(qMax)

qs = [x for x in filter(lambda k: k%4 == 1 ,primes)]
ps = [2] + [x for x in filter(lambda k: k%4 == 3 and k <= pMax ,primes)]
qs.sort()
ps.sort()


##some cutoffs
Nd=biggestN/(5*5*13)
N5=biggestN/5
N52=biggestN/5**2
N53=biggestN/5**3



len_c = biggestN // (5**3*13**2*17) + 1
##want choices[N//t] to be the number of combs of 2 and p's that give t*(2 and p) < N
choices = [False] * len_c ##if this is true, plus one choice
choices[1] = True ##the empty product
for p in ps:
    if p >= len_c: break
    choices[p] = True ##there always the choice to add a p
for i in range(3, len_c, 2):
    if choices[i]: continue
    l = math.sqrt(i)
    for p in primes:
        if p > l: ##p wont divide i if this is the case
            break
        if i % p == 0: ##this is the point where it increments
            if p % 4 == 3: ##if its a prime in ps
                choices[i] = choices[i//p]
            break
for i in range(1, (len_c+1)//2):
    choices[i*2] = choices[i]
combs = [0] * len_c
currentSum = 0
for i, f in enumerate(choices):
    if f: currentSum += i ##for every true, there was a p=4k+3 that was able to multiply i=t/p
    combs[i] = currentSum

answer = 0


for i in range(len(qs)):
    v3 =qs[i]**3
    if v3 > Nd:
        break
    for j in range(len(qs)):
        if i == j:
            continue
        v2 = qs[j]**2
        if v3*v2> N5:
            break
        for k in range(len(qs)):
            if k == i or k == j:
                continue
            val = v3*v2*qs[k]
            if val > biggestN:
                break
            answer += val*combs[biggestN//val]

for i in range(len(qs)):
    v7 =qs[i]**7
    if v7 > N53:
        break
    for j in range(len(qs)):
        if i == j:
            continue
        val = v7*qs[j]**3
        if val > biggestN:
            break
        answer += val*combs[biggestN//val]

for i in range(len(qs)):
    v10 =qs[i]**10
    if v10 > N52:
        break
    for j in range(len(qs)):
        if i == j:
            continue
        val = v10*qs[j]**2
        if val > biggestN:
            break
        answer += val*combs[biggestN//val]


print(answer)


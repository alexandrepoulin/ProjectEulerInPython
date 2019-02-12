print("Starting")

import useful
import math

MAX = 10**8

#pi(5000000)=3001134
#pi(10^8/3)=2050943
#pi(10^8/5)=1270607
#pi(10^8/7)= 927432
#pi(10^8/11)= 608113
#pi(10^8/13)= 520415
#pi(10^8/17)= 405279
#pi(10^8/19)= 365522
#pi(10^8/23)= 305944
#pi(10^8/29)= 246788

answer = 3001134+2050943-1+1270607-2+927432-3+608113-4+520415-5+405279-6+365522-7+305944-8+246788-9
subFact = 9

primes = useful.primesTo(int(4*10**6))
primes.sort()

summingPrimes = primes[10:1229]
for p in summingPrimes:
    primes = [x for x in filter(lambda k: k <= MAX/p,primes)]
    subFact += 1
    answer += len(primes) - subFact


print(answer)
input("Done")

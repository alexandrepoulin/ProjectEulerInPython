print("starting")
import useful

primes = useful.primesTo(10**6)

def layer(n): ##nth layer, gives starts
    if n == 0 :
        return 1
    return 3*n**2-3*n+2

inner = 0
middle = 1
outer = 2
outer2 = 8
nm = 0

answer = 0
answerLen = 2000

counter = 1

while True:
    nm+=1
    inner = middle
    middle = outer
    outer = outer2
    outer2 = layer(nm+2)
    good = True
    
    if (outer-1 - middle) in primes:
        pass
    else:
        continue
    if (outer+1 - middle) in primes:
        pass
    else:
        good = False
    if good and (outer2-1 - middle) in primes:
        pass
    else:
        good = False
    if good:
        counter += 1
        if (counter%10) == 0:
            print(counter)
        if (counter % answerLen) == 0:
            answer = middle
            break
    
    good = True
    if (outer-1-inner) in primes:
        pass
    else:
        good = False
    if good and (outer2-1 - outer) in primes:
        pass
    else:
        good = False
    if good:
        counter +=1
        if (counter%10) == 0:
            print(counter)
        if (counter % answerLen) == 0:
            answer = outer-1
            break

print(answer)

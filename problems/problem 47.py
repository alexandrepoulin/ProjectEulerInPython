
print("Starting")

import useful

answer = 0
counter = 2

def compressFactors(x):
    factors = set(x)
    answer = []
    for y in factors:
        answer.append(y**(x.count(y)))
    return answer



def main():
    counter = 2*3*5*7
    primes = useful.primesTo(1000)
    fact1 = [2,3,5,7]
    fact2 = [compressFactors(useful.factorsFromPrimes(counter+1,primes))]
    fact3 = [compressFactors(useful.factorsFromPrimes(counter+2,primes))]
    fact4 = [compressFactors(useful.factorsFromPrimes(counter+3,primes))]
    while True:
        #print(counter)
        if len(fact4)!= 4:
            counter += 4
            fact1 = compressFactors(useful.factorsFromPrimes(counter,primes))
            fact2 = compressFactors(useful.factorsFromPrimes(counter+1,primes))
            fact3 = compressFactors(useful.factorsFromPrimes(counter+2,primes))
            fact4 = compressFactors(useful.factorsFromPrimes(counter+3,primes))
            continue
        if len(fact3) != 4:
            counter+=3
            fact1 = fact4
            fact2 = compressFactors(useful.factorsFromPrimes(counter+1,primes))
            fact3 = compressFactors(useful.factorsFromPrimes(counter+2,primes))
            fact4 = compressFactors(useful.factorsFromPrimes(counter+3,primes))
            continue
        if len(fact2) != 4:
            counter+=2
            fact1 = fact3
            fact2 = fact4
            fact3 = compressFactors(useful.factorsFromPrimes(counter+2,primes))
            fact4 = compressFactors(useful.factorsFromPrimes(counter+3,primes))
            continue
        if len(fact1) != 4:
            counter+=1
            fact1 = fact2
            fact2 = fact3
            fact3 = fact4
            fact4 = compressFactors(useful.factorsFromPrimes(counter+3,primes))
            continue
        if len(set(fact1+fact2+fact3+fact4)) == 16:
            answer = counter
            break
        else:
            counter+=1
            fact1 = fact2
            fact2 = fact3
            fact3 = fact4
            fact4 = compressFactors(useful.factorsFromPrimes(counter+3,primes))
    print(answer)
    input("Done")

if __name__ == '__main__':
    main()
        
    

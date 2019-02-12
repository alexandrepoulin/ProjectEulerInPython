print("Starting")

MAX = 1000000

numbers = set(range(MAX,1,-1))

primes = []

while numbers:
    p = numbers.pop()
    primes.append(p)
    numbers.difference_update(set(range(p*2, MAX+1, p)))

bestStreak = 0
bestPrime = 0

print("Done finding primes")
##len(primes) = 78498

done = False

while len(primes)>0:
    print(len(primes))
    p = primes[0]
    sumSoFar = 0
    currentStreak = 0
    counter = 0
    while True:
        if currentStreak+counter >= len(primes):
            break
        done = p*bestStreak > MAX
        sumSoFar += primes[currentStreak+counter]
        if sumSoFar > MAX:
            break
        if sumSoFar in primes:
            currentStreak += 1 + counter
            counter = 0
            if currentStreak > bestStreak:
                bestStreak = currentStreak
                bestPrime = sumSoFar
        else:
            counter+=1
    primes.remove(p)
    if done:
        break
    
print(bestPrime)
print(bestStreak)

input("Done")

#find the 10 001 prime

print("Starting...")

primes = [2]

currentlength = 1

counter = 3

isCounterPrime = True

while currentlength < 10001:
    for int in range(currentlength):
        if counter%primes[int] == 0:
            isCounterPrime = False
            break
    if isCounterPrime:
        primes.append(counter)
        currentlength+=1
    counter+=2
    isCounterPrime = True
    if currentlength%1000 == 0:
        print(currentlength)
    

print(primes[-1])

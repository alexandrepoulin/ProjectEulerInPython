#find the sum of all the primes below 2 million

print("Starting...")

numbers = set(range(2000000,1,-1))


sum = 0

while numbers:
    p = numbers.pop()
    sum+=p
    numbers.difference_update(set(range(p*2, 2000000+1, p)))
    
    
print(sum)

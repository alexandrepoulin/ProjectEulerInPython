print("Starting")

import useful
MAX = 31623 ##10^9/2 rounded up
primes = useful.primesTo(31623)

nums = [1,2,3,4,5,6,7,8,9]
perms = useful.perm(nums)

success = []

def test(numbersLeft,solution): ##the permutation and the set
    length = len(numbersLeft)
    if length == 0 and solution not in success:
        success.append(solution)
        return
    for i in range(1,length+1):
        number = useful.listToInt(numbersLeft[:i])
        tempSol = solution.copy()
        if useful.fastIsPrime(number,primes,MAX):
            tempSol.add(number)
            test(numbersLeft[i:],tempSol)
    
current = 0
for i in range(len(perms)):
    if (i%1000) ==0:
        print(i, " out of ", len(perms))
    test(perms[i],set())

print(len(success))
input("Done")

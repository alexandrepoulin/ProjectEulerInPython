import time
print("Starting")
now = time.time()

possi = []

def nextSet(x):
    nums = list(x)
    nums.sort()
    for i in range(0,6):
        if nums[-i-1] != 9 and nums[-i-1]+1 not in nums:
            nums[-i-1] += 1
            for k in range(0,i+1):
                nums[-i-1+k] = nums[-i-1]+k
            break
    return set(nums)

def check(c1,c2):
    if (0 in c1 and 1 in c2) or (0 in c2 and 1 in c1):
        if (0 in c1 and 4 in c2) or (0 in c2 and 4 in c1):
            if (0 in c1 and (9 in c2 or 6 in c2)) or (0 in c2 and (9 in c1 or 6 in c1)):
                if (1 in c1 and (9 in c2 or 6 in c2)) or (1 in c2 and (9 in c1 or 6 in c1)):
                    if (2 in c1 and 5 in c2) or (2 in c2 and 5 in c1):
                        if (3 in c1 and (9 in c2 or 6 in c2)) or (3 in c2 and (9 in c1 or 6 in c1)):
                            if (4 in c1 and (9 in c2 or 6 in c2)) or (4 in c2 and (9 in c1 or 6 in c1)):
                                if (8 in c1 and 1 in c2) or (8 in c2 and 1 in c1):
                                    return True
    return False

c1 = set()
nextC1 = {0,1,2,3,4,5}

while nextC1 != c1:
    c1 = nextC1
    c2 = set()
    nextC2 = {0,1,2,3,4,5}
    while nextC2 != c2:
        c2 = nextC2
        if check(c1,c2):
            if [c1,c2] not in possi and [c2,c1] not in possi:
                possi.append([c1,c2])
        nextC2 = nextSet(c2)
    nextC1 = nextSet(c1)

print(len(possi))
end = time.time()
print(end-now)
        
#other#
from itertools import combinations
now=time.time()
print(sum(all(((d1 in c1 and d2 in c2) or (d2 in c1 and d1 in c2))
          for d1, d2 in ((0,1),(0,4),(0,6),(1,6),(2,5),(3,6),(4,6),(8,1)))
          for c1, c2 in combinations(combinations(list(range(9))+[6], 6), 2)))
end=time.time()
print(end-now)


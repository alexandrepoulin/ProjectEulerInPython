import itertools

nums = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]

num67 = [x for x in itertools.combinations(nums,10) if sum(x)==67] ##44
num56 = [x for x in itertools.combinations(nums,10) if sum(x)==56] ##22
num45 = [x for x in itertools.combinations(nums,10) if sum(x)==45] ##0
num34 = [x for x in itertools.combinations(nums,10) if sum(x)==34] ##-22
num23 = [x for x in itertools.combinations(nums,10) if sum(x)==23] ##-44

##num67.sort()
##num56.sort()
##num45.sort()
##num34.sort()
##num23.sort()
##
##num67 = list(set(num67))
##num56 = list(set(num56))
##num45 = list(set(num45))
##num34 = list(set(num34))
##num23 = list(set(num23))
##
##nums = [num67,num56,num45,num34,num23]
##
##for s in nums:
##    for n in s:
##        n=list(n)
##        n.sort()
num67 = set(num67)
num56 = set(num56)
num45 = set(num45)
num34 = set(num34)
num23 = set(num23)

nums = [num67,num56,num45,num34,num23]

total = 0

for s in nums:
    for n in s:
        q = 10-len(set(n))
        p = n.count(0)
        total+=((10-p)*1316818944000>>(2*q))
print(total)

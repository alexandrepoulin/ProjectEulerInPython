import useful as u


nums = dict()

for x in range(2,30000):
    if x%1000==0:
        print(x)
    for y in range(2,1000):
        val = x**2+y**3
        if u.isPal(val):
            if val in nums.keys():
                nums[val]+=1
            else:
                nums[val]=1

exactly4 = []
for k,v in nums.items():
    if v==4:
        exactly4.append(k)

exactly4.sort()
print(sum(exactly4[:5]))
print(exactly4)


##this is just related to the sum of the fibonacci numbers
l=[0,1,1]
for n in range(3,31):
    l.append(l[-1]+l[-2])

##plus one for 2**30
print(sum(l)+1)

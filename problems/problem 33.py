print("Starting")

total = 0
goodNums = []
for i in range(10,100):
    for j in range(10,100):
        if i %10 == 0 and j % 10 ==0:
            continue
        if i %11 == 0 and j % 11 ==0:
            continue
        if i >= j :
            continue
        nums = [i,j]
        index = []
        if (str(i)[0] == str(j)[0]):
            index.append([0,0])
        if (str(i)[0] == str(j)[1]):
            index.append([0,1])
        if (str(i)[1] == str(j)[0]):
            index.append([1,0])
        if (str(i)[1] == str(j)[1]):
            index.append([0,1])
        if len(index) == 0:
            continue
        for k in range(0,len(index)):
            print(nums[(index[k][0]+1) % 2]/nums[(index[k][1]+1) % 2] == nums[0]/nums[1])
            print(index)
            print(nums)
            nom = str(nums[0])
            denom = str(nums[1])
            if int(denom[(index[k][1]+1) % 2]) == 0 :
                continue
            if int(nom[(index[k][0]+1) % 2]) / int(denom[(index[k][1]+1) % 2]) == nums[0]/nums[1]:
                goodNums.append(nums)
        

print(goodNums)

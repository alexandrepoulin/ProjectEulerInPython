#20161
print("Starting...")

def isAbun(x):
    sumSoFar = 0
    for i in range(1,x):
        if x % i == 0 :
            sumSoFar += i
    return sumSoFar > x

def removeTerms(x,a,b):
    x.difference_update(set(range(a,20162,b)))
    return x   

def answer(x):
    #myfile = open("test2.txt","w")
    answer = 0
    removed = []
    integers = set(range(x))
    intEdit = set(range(x))
    simpleAbunNum = []
    counter = 0
    counter2 = 1
    counter3 = 1
    #myfile.writelines(str(integers) + "\n")
    while intEdit:
        print(len(intEdit))
        i = intEdit.pop()
        if isAbun(i):
            simpleAbunNum.append(i)
            integers = removeTerms(integers,2*i,i)
            intEdit = removeTerms(intEdit,2*i,i)
    #myfile.writelines(str(integers) + "\n")
    for j in simpleAbunNum:
        print(len(simpleAbunNum) - counter)
        for k in simpleAbunNum[counter:]:
            while counter2*j+counter3*k < x+1:
                while counter2*j+counter3*k < x+1:
                    integers = removeTerms(integers,0,counter2*j+counter3*k)
                    counter3 +=1
                counter3 = 1
                counter2 +=1
            counter2 = 1
        counter +=1
    for j in integers:
        print(j)
        #myfile.writelines(str(j) + "\n")
        answer += j
    #myfile.close()
    return answer


print(answer(20162))

input("Here You go")


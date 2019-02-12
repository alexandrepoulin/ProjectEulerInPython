
numCarts = 11
arrange = 2011

solForN=[[],[[1]],[[2,1]]]

def solToLet(x):
    return "".join([x for x in map(lambda k: chr(64+k),x)])
    

for i in range(3,numCarts+1):
    currentSol=[]
    for s in solForN[i-1]:
        temp = [1]+[x for x in map(lambda k: k+1, s)]
        temp=temp[::-1]
        for j in range(1,i-1):
            currentSol.append(temp[:j]+temp[-1:j-1:-1])
    solForN.append(currentSol)
    print(len(currentSol))

temp=solForN[numCarts]
temp.sort()
print(solToLet(temp[arrange-1]))

print("Starting")

def inList(x,y):
    for i in x:
        if i == y:
            return True
    return False

answerList = []
for a in range (2,101):
    print(a)
    for b in range (2,101):
        if not inList(answerList, a**b):
            answerList.append(a**b)

print(len(answerList))
        

input("Press anything to close")

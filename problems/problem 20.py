print("Starting...")

def fact(x):
    answer = 1
    for i in range(1,x+1):
        answer *= i
    return answer

def sumOfTerms(x):
    sumSoFar = 0
    for i in range(0, len(str(x))):
        sumSoFar += int(str(x)[i])
    return sumSoFar

print(sumOfTerms(fact(100)))

input("Press enter to exit")

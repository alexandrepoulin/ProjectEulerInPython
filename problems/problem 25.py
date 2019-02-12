print("Starting")

def answer(n):
    fibNum = [1,1]
    counter = 2
    currentNumber = fibNum[1]
    lenght = len(str(currentNumber))
    while lenght < n:
        counter += 1
        currentNumber = fibNum[len(fibNum)-1] + fibNum[len(fibNum)-2]
        fibNum.append(currentNumber)
        lenght = len(str(currentNumber))
    return counter;

print(answer(1000))

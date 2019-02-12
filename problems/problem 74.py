print("Starting")

factorials = [1,1,2,6,24,120,720,5040,40320,362880]

def nextVal(x):
    stringOfNumber = str(x)
    answer = 0
    for digit in stringOfNumber:
        answer += factorials[int(digit)]
    return answer

numbers = [x for x in range(1000000,0,-1)]

counter = 0

for num in numbers:
    print(num)
    values = [num]
    while True:
        nextValue = nextVal(values[-1])
        if nextValue in values and len(values) == 60:
            counter +=1
            break
        if nextValue in values:
            break
        values.append(nextValue)
        
print(counter)
input("Done")

        

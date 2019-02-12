print("starting")

number = "."
currentNumber = 0

while len(number)<1000002:
    print(len(number))
    currentNumber += 1
    number += str(currentNumber)

print(int(number[1])*int(number[10])*int(number[100])*int(number[1000])*int(number[10000])*int(number[100000])*int(number[1000000]))
input("asdfasf")

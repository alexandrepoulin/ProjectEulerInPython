print("Starting")
import math

MAX = 10**15

def D(x):
    return 3*x
def U(x):
    return (3*x-2)/4
def d(x):
    return (3*x+1)/2

def string(code):
    x = 1
    for i in range(len(code)-1,-1,-1):
        while True:
            temp = x
            if code[i] == 'D':
                temp = D(x)
            if code[i] == 'U':
                temp = U(x)
            if code[i] == 'd':
                temp = d(x)
            if int(temp) != temp:
                x+=3**(len(code)-i)
            else:
                x=temp
                break
    return x

def answer(code):
    x = string(code)
    power = 3**(len(code))
    return math.ceil(MAX/power)*power+(x%(power))
    
print(answer("UDDDUdddDDUDDddDdDddDDUDDdUUDd"))

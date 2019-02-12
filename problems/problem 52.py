print("Starting")

found = False

num = 100
power = 2

while not found:
    num +=1
    if int(str(num)[0]) > 10**(power+1)/6:
        power +=1
        num = 10**power
    found = set(str(num)) == set(str(2*num))and set(str(2*num)) == set(str(3*num)) and set(str(3*num)) == set(str(4*num)) and set(str(4*num)) == set(str(5*num)) and set(str(5*num)) == set(str(6*num))

for i in range(1,7):
    print(i*num)


input("something")

print("Starting")
Sum = 0
for i in range(1,10):
    if i%2 == 0 :
        Sum += 20*30**(i/2-1)
    elif i%4 == 3:
        Sum += 5*20*(500**((i-3)/4))

print(Sum)

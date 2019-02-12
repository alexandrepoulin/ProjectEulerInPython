print("starting")

counter = 10**9+10**7+10**5+10**3+70

while True:
    counter += 100
    val = counter**2
    print(val)
    if str(val)[::2] == "1234567890":
        break
    if str(val)[:3] !="192":
        counter+=10000

print(counter)

input("Done")
    

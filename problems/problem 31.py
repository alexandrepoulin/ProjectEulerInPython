print("Starting")

total = 1

for j in range(0,3):
    for k in range(0,5):
        for l in range(0,11):
            for m in range(0,21):
                for q in range(0,41):
                    for n in range(0,101):
                        for p in range(0,201):
                            number = j*100+k*50+l*20+m*10+q*5+n*2+p
                            if number > 200:
                                break
                            if number == 200:
                                total += 1
                                break
                                

print(total)
input("press something")

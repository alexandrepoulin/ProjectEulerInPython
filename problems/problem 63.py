print("Starting")


counter = 0

for i in range(1,10):
    k = 0
    val = ""
    while k <= len(str(val)):
        k+=1
        val = i**k
        if len(str(val)) == k:
            counter+=1

print(counter)
input("done")

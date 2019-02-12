print("Starting")

def f(n,r):
    answer = 1
    lower = max(r, n-r)
    upper = min(r, n-r)
    for i in range(upper+1,n+1):
        answer*=i
    for i in range(2, lower+1):
        answer*=(1/i)
    return int(answer)

count = 0

for n in range(1,101):
    print(n)
    for r in range(1,n):
        if f(n,r) > 1000000:
            count+= n-2*r+1
            break

print(count)
input("done")

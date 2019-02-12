print("starting")

def pentagonal(n): return (n * (3 * n - 1) ) >>1 # the nth pentagonal number is given by (3n^2 - n)/2
 
def generalised_pentagonal(n): # 0, -1, 1, -2, 2
    if n & 1 == 0:
        return pentagonal((n >> 1) + 1)  # pentagonal(n/2 + 1) if n is even
    else:
        return pentagonal(-(n >> 1) - 1) # pentagonal(-(n/2 + 1)) if n is odd
 
def termsign(i):
    if i & 3 < 2:
        return 1 # add if i mod 4 is 0 or 1
    else:
        return -1 # subtract otherwise
 
pt = [1]
counter = 0
while True:
    print(counter)
    counter += 1
    n = counter
    r, i = 0, 0
    while True:
        k = generalised_pentagonal(i)
        if k > n: 
            break
        r += termsign(i) * pt[n - k]
        i += 1
    pt.append(r)
    if counter == 100:
        break
    
print(pt[-1]-1)
input("Done")

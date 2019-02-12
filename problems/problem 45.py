print("Starting")

n = 286
m = 166
j = 144

def tri(n):
    return n*(n+1)/2
def pent(n):
    return n*(3*n-1)/2
def hexa(n):
    return n*(2*n-1)

while tri(n) != pent(m) or pent(m) != hexa(j):
    if tri(n) < pent(m) or tri(n)< hexa(j):
        n += 1
    elif pent(m) < tri(n) or pent(m) < hexa(j):
        m += 1
    elif hexa(j) < tri(n) or hexa(j) < pent(m):
        j += 1

print(tri(n))
print(pent(m))
print(hexa(j))

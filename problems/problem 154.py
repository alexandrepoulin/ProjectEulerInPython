print("Starting")

counter = 0
MAX = 200000

def multiNom(i,j):
    answer = 1
    l1 = max(i,j,MAX-i-j)
    l2 = min(i,j,MAX-i-j)
    l3 = 0
    if (l1 == i and l2 == j) or (l1 == j and l2 == i):
        l3 = MAX - i - j
    elif l1 == i and l2 != j:
        l3 = j
    else:
        l3 = i
    for p in range(l1+1,MAX+1):
        answer  *= p
    for q in range(1,l2+1):
        answer /= q**2
    for r in range(l2+1,l3+1):
        answer /= r
    return answer 

for i in range(MAX):
    for j in range(Max//2):
        if multiNom(i,j)%10**12:
        

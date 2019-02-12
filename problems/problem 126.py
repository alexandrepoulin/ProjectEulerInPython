##layers are defined by 3 parameters
##L = length at widest
##H = heigth at widest
##C = cutoff (widest minus smallest /2)

##for a given (L,H,C), the number of cubes addeds is:
##N(L,H,C) = 2*(L+H-4*C)+4*C =2*(L+H-2*C)
##each layer gives L->L+2, H->H+2,C->C+1
##We start with a cube which is L*H*P where P is the number of layers

##In the first cover, we have P*N(L,H,0)+2*L*N
##This new object has P (L+2,H+2,1) layers, and 2 (L,H,0) layers
##In general, the nth covering will be an object with
##P(L+2n, H+2n,n) , 2: (L+2(n-1), H+2(n-1),(n-1)), (L+2(n-2), H+2(n-2),(n-2)), ... (L,H,0)
##So to cover the nth layer, we need
##B= P*N(L+2n, H+2n,n)+2*sum_k=0^(n-1) N(L+2k, H+2k,k) + 2*L*H
##B = 2*(P+2n)*(L+H)+4*(n-1)n+2LH+4nP
## note n=0 gives you the number for the initial layer

def B(L,H,P,n):
    return 2*(P+2*n)*(L+H)+4*(n-1)*n+2*L*H+4*n*P

##we want to find values of L,H,P,n such that B = 1000
##we limit L*H*P < 1000

answers = dict()

assumedMax = 20000 ##makes the space manageable

for L in range(1,assumedMax):
    for H in range(1,L+1):
        if 2*H*L+2*(H+L) > assumedMax:
            break
        for P in range(1,H+1):
            if 2*(L*P+L*H+H*P) > assumedMax:
                break
            for n in range(0,assumedMax):
                val = B(L,H,P,n)
                if val >assumedMax:
                    break
                if val in answers:
                    answers[B(L,H,P,n)] += 1
                else:
                    answers[B(L,H,P,n)] = 1
print("done Looping")

possible = []
for j in answers:
    if answers[j] == 1000:
        possible.append(j)

print(min(possible))

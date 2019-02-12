
import useful as u

N=7
k=3

tot=0
for a in range(1,k+1):
    if (k-a)%2 == 1:
        continue
    b=((a-k)>>1)
    tot += u.nChooseK(N,a)+u.nChooseK(N-a,b)
tot/=N**k

print(tot)



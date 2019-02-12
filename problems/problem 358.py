import useful as u

p=729809891 ##this has to be the generating prime 


tot = ((p-1)//10)*45
for i in range((p-1)%10+1):
    tot+=9*i%10
print(tot)


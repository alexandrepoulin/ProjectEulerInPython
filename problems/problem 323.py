import useful as u

maxIndex = 32

expected = [0]

for i in range(1,maxIndex+1):
    temp=0
    for j in range(0,i):
        temp += u.nChooseK(i,j)*expected[j]
    temp*=1/(2**i-1)
    temp+=2**i/(2**i-1)
    expected.append(temp)
print(expected[32])

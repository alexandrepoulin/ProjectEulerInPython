
def e(n):
    answer = 0
    for i in range(1,n+1):
        answer += (2**(i-1)-1)/i
    return answer

print(e(30))

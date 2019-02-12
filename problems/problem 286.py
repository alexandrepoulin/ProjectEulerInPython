import random

def scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest

easiest = list(range(1,21))
easiestC = list(range(21,51))
hardest = list(range(30,51))
hardestC = list(range(1,31))

full = list(range(1,51))
rand = scrambled(full)[:20]
randC = [x for x in filter(lambda k: k not in rand,full)]



def randomP(inList,inListC, q):
    answer = 1
    for x in inList:
        answer *= (1 - x/q)
    for y in inListC:
        answer *= y/q
    return answer

def upper(q):
    answer = 1
    for x in easiest:
        answer *= (1 - x/q)
    for y in easiestC:
        answer *= y/q
    return answer

def lower(q):
    answer = 1
    for x in hardest:
        answer *= (1 - x/q)
    for y in hardestC:
        answer *= y/q
    return answer

print(upper(51),randomP(rand,randC,51),lower(51))
print(upper(100),randomP(rand,randC,100),lower(100))
print(upper(150),randomP(rand,randC,150),lower(150))

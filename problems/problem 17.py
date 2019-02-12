print("Starting...")

x1 = 3
x2 = 3
x3 = 5
x4 = 4
x5 = 4
x6 = 3
x7 = 5
x8 = 5
x9 = 4

OneToTen = x1+x2+x3+x4+x5+x6+x7+x8+x9

x10 = 3
x11 = 6
x12 = 6
x13 = 8
x14 = 8
x15 = 7
x16 = 7
x17 = 9
x18 = 8
x19 = 8

tenToNineteen = x10+x11+x12+x13+x14+x15+x16+x17+x18+x19

x20 = 6
x30 = 6
x40 = 5 
x50 = 5
x60 = 5
x70 = 7
x80 = 6
x90 = 6
hund = 7
xand = 3
x1000 = 11

oneTo99 = OneToTen*9+tenToNineteen+x20*10+x30*10+x40*10+x50*10+x60*10+x70*10+x80*10+x90*10
answer = 100*OneToTen+900*hund+xand*99*9+10*oneTo99+x1000

print(answer)

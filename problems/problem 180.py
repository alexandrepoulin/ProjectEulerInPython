print("Starting")

import useful
from collections import defaultdict

from mpmath import *
mp.pretty = True
mp.dps = 100
sigfigs = 100


maxN = 100
k = 10

nvals = defaultdict(dict)
for nom in range(1,k):
    for denom in range(nom+1,k+1):
        for n in range(-maxN-2,maxN+2):
            nvals[nom/denom][n] = power(fdiv(nom,denom),n)
print("done making nVals")
def f1(x,y,z,n):
    return nvals[x][n+1]+nvals[y][n+1]-nvals[z][n+1]
def f2(x,y,z,n):
    return (x*y+y*z+z*x)*(nvals[x][n-1]+nvals[y][n-1]-nvals[z][n-1])
def f3(x,y,z,n):
    return x*y*z*(nvals[x][n-2]+nvals[y][n-2]-nvals[z][n-2])
def f(x,y,z,n):
    return f1(x,y,z,n)+f2(x,y,z,n)+f3(x,y,z,n)

def s(xn,xd,yn,yd,zn,zd):
    denom = xd*yd*zd
    nom = xn*yd*zd+xd*yn*zd+xd*yd*zn
    g = useful.GCD(nom,denom)
    return [int(nom/g),int(denom/g)]

sVals = []

for xn in range(1,k):
    print("xn = ", xn)
    for xd in range(xn+1,k+1):
        print("xd = ", xd)
        if useful.GCD(xn,xd) !=1:
            continue
        x = xn/xd
        for yn in range(1,k):
            for yd in range(yn+1,k+1):
                if useful.GCD(yn,yd) !=1:
                    continue
                y = yn/yd
                if y < x:
                    break
                for zn in range(1,k):
                    for zd in range(zn+1,k+1):
                        if useful.GCD(zn,zd) !=1:
                            continue
                        z = zn/zd
                        for n in range(-maxN,maxN):
                            if abs(f(x,y,z,n)) == 0:
                                sValsTemp = s(xn,xd,yn,yd,zn,zd)
                                print(n, xn,xd,yn,yd,zn,zd,sValsTemp)
                                if sValsTemp not in sVals:
                                    sVals.append(sValsTemp)
                                break

u = 0
v = 1
for f in sVals:
    denom = v*f[1]
    nom = v*f[0]+u*f[1]
    g = useful.GCD(nom,denom)
    u = nom/g
    v = denom/g
print(len(sVals))
print(u+v)

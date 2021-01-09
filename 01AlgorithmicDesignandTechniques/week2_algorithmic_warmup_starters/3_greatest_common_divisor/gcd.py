# Uses python3
import sys
from random import randint

def gcd_naive(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

# print(gcd_naive(17,0))




# efficient algorithm
def gcd_efficient(a,b):
    if b == 0:
        return a
    if a == 0:
        return b
    remainder = a % b
    return gcd_efficient(b,remainder)

# print(gcd_efficient(17,0))

def stress_test(N,M):
    while True:
        n = randint(0,N)
        m = randint(0,M)
        if gcd_efficient(n,m) == gcd_naive(n,m) and gcd_efficient(m,n) == gcd_naive(m,n):
            print('working')
        else:
            print('Not working',n,m)
            return

stress_test(20000000,20000000)
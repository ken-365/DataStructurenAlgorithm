# Uses python3
import sys
from random import randint
from timeit import default_timer as timer

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     a, b = map(int, input.split())
#     print(lcm_naive(a, b))

# efficient
def lcm_efficient(a,b):
    def gcd_efficient(a,b):
        if b == 0:
            return a
        if a == 0:
            return b
        remainder = a%b
        return gcd_efficient(b,remainder)
    GCD =  gcd_efficient(a,b)
    return int((a*b) / GCD)

# start = timer()
# print(lcm_naive(65454,15321))
# end = timer()
# print('naive',end - start)



def stress_test(N,M):
    while True:
        n = randint(0,M)
        m = randint(0,N)
        if lcm_efficient(n,m) == lcm_naive(n,m) and lcm_efficient(m,n) == lcm_naive(m,n):
            print('working')
        else:
            print('Not working',n,m)
            return

# stress_test(9999999999999,10000000)
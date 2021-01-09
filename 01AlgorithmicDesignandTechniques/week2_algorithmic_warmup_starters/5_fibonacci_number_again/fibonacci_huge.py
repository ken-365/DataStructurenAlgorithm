# Uses python3
import sys
from random import randint
from timeit import default_timer as timer

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

# if __name__ == '__main__':
#     input = sys.stdin.read();
#     n, m = map(int, input.split())
#     print(get_fibonacci_huge_naive(n, m))

# efficient algorithm (recursive sign)


def get_fibonacci_efficient(n):
    F = [None] * (n+1)
    F[0] =0 
    F[1] = 1
    for i in range(2,n+1):
        F[i] = F[i-1] + F[i-2]
    return F[i]


def get_fibonacci_huge_efficient(n,m):
    repeat_period = 0
    for i in range(3,m*m+1):
        if (get_fibonacci_efficient(i)%m)  == 0 and (get_fibonacci_efficient(i+1)%m) ==1 and \
            (get_fibonacci_efficient(i+2)%m) ==1:
            repeat_period = i  # plus 1 because python count from zero
            break
    # then compute remainder
    remainder  = n % repeat_period
    return get_fibonacci_efficient(remainder) % m




# copy ma
def get_fibonacci(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current
def fib_period_length(m):
    previous = 0
    current = 1
    for i in range(m * m + 1):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1
def get_fibonacci_huge_fast(n, m):
    remainder = n % fib_period_length(m)
    return get_fibonacci(remainder) % m




def test_runtime(n,m):
    # start = timer()
    # get_fibonacci_huge_naive(n,m)
    # end = timer()
    # print('naive',end - start)

    start = timer()
    get_fibonacci_huge_efficient(n,m)
    end = timer()
    print('my approach',end - start)

    start = timer()
    get_fibonacci_huge_fast(n,m)
    end = timer()
    print('internet copy ma approach',end - start)

test_runtime(5248888865554,4655)


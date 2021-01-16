# Uses python3
import sys

def get_change_naive(m):
    count = 0
    while m>0:
        if m > 10 :
            m -= 10
            count +=1
        elif m> 5:
            m -= 5
            count += 1
        elif m> 0:
            m-= 1
            count += 1
        else:
            break
    return count

# efficient
def get_change_specific(value):
    p, n, d = 1, 5, 10
    count = 0
    while value > 0:
        if value >= d:
            count += value // d
            value %= d
        elif value >= n:
            count += value // n
            value %= n
        else:
            count += value // p
            break
    return count

# print(get_change_naive(654))
# print(get_change_specific(654))
from random import randint

def stress_test(M):
    m = randint(0,M)
    while True:
        if get_change_naive(m) == get_change_specific(m):
            print('OK')
        else:
            return (get_change_naive(m),get_change_specific(m),m,'not ok')
            break

# stress_test(9098400)


def get_change(m):
    #Greedy start minus 10 (divide)until m is less than 10 then 5 and 1

    return m

# if __name__ == '__main__':
#     m = int(sys.stdin.read())
#     print(get_change(m))

import time

start_time = time.time()
print('answer is',get_change_specific(5646515555555454), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print('answer is',get_change_naive(5646515555555454), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))
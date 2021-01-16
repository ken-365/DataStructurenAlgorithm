# Uses python3
import sys
import time
def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
#     print(fibonacci_sum_naive(n))

def fibonacci_sum_efficient(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    previous = 0
    current = 1
    sum = 1
    for i in range(n-1):
        previous, current = current, (previous + current) %10
        sum += current
    return sum%10

# try in excel there is pisano period of the last digit of sum of fibonacci that start with 01 every 60 sequence number
# pretend we know only pisano start with 0 and then 1

def fibonacci_fast(n):
    # find pisano period
    if n == 0:
        return 0
    if n == 1:
        return 1
    previous = 0
    current = 1
    sum = 1
    result_list = [0,1]
    for i in range(n-1):
        previous, current = current, (previous + current) %10
        sum += current
        result_list.append(sum%10)
        if sum %10 == 0 :
            if(sum+current+previous)%10 ==1 :
                pisano = i+1
                break
    # if n < 60 then can grap from list, else have to mod 60 to get from list
    if n< 60:
        return result_list[n]
    else:
        return result_list[n%(pisano+1)]  


# start_time = time.time()
# print('answer is',fibonacci_sum_naive(888888), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))

# start_time = time.time()
# print('answer is',fibonacci_sum_efficient(888888), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))

# start_time = time.time()
# print('answer is',fibonacci_fast(888888), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))

# stress test 
from random import randint
def stress_test(N):
    n = randint(0,N)
    while True:
        if fibonacci_fast(n) == fibonacci_sum_efficient(n):
            print('ok')
        else:
            print('Not ok', n)
            return

stress_test(999999)
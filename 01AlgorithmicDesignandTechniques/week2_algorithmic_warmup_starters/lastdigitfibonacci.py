# find F at 'n' position
# import time
# start_time = time.time()

# def calc_lastfib(n):
#     alist = [None] * (n+1)
#     alist[0] = 0
#     alist[1] = 1
    
#     for i in range(2,n+1):
#         alist[i] = (alist[i-1] + alist[i-2])%10
#     return alist[n]
# # n = int(input())
# # print(calc_lastfib(n))

# print('answer is',calc_lastfib(3), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))
# print('answer is',calc_lastfib(331), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))
# print('answer is',calc_lastfib(327305), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))

# for submission

# Uses python3
import sys

def get_fib_last(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    F = [None] * (n+1)
    F[0] = 0
    F[1] = 1

    for i in range(2,n+1):
        F[i] = (F[i-1]+F[i-2]) % 10
    return F[n]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fib_last(n))

# find F at 'n' position
# import time
# start_time = time.time()
# def fibonacci(n):
#     alist = [None]*(n+1)
#     alist[0] = 0
#     alist[1] = 1
 
#     for i in range(2,n+1):
#         alist[i] = alist[i-1] + alist[i-2]
#     return alist[n]

# n = int(input())
# print(fibonacci(n))
# print("--- %s seconds ---" % (time.time() - start_time))


# print('answer is',fibonacci(10), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))
# print('answer is',fibonacci(200), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))

# for submission

# Uses python3
import sys
def fib_submit(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    F = [None] * (n+1)
    F[0] = 0
    F[1] = 1

    for i in range (2,n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]
n = int(input())
print(fib_submit(n))


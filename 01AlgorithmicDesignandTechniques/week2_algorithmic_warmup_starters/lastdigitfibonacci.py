# find F at 'n' position
import time
start_time = time.time()

def calc_lastfib(n):
    alist = [None] * (n+1)
    alist[0] = 0
    alist[1] = 1
    
    for i in range(2,n+1):
        alist[i] = (alist[i-1] + alist[i-2])%10
    return alist[n]
# n = int(input())
# print(calc_lastfib(n))

print('answer is',calc_lastfib(3), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))
print('answer is',calc_lastfib(331), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))
print('answer is',calc_lastfib(327305), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))
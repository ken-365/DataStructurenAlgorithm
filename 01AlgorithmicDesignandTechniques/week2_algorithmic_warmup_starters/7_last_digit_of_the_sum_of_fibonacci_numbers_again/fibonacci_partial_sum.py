# Uses python3
import sys

def fibonacci_partial_total_naive(from_, to):
    total = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            total += current

        current, next = next, current + next

    return total % 10


# if __name__ == '__main__':
#     input = sys.stdin.read();
#     from_, to = map(int, input.split())
#     print(fibonacci_partial_total_naive(from_, to))


def fibonacci_partial_sum(m,n):
    # find pisano period
    if n == 0:
        return 0
    if n == 1:
        return 1
    previous = 0
    current = 1
    total = 1
    result_list2 = [0,1]
    for i in range(n-1):
        previous, current = current, (previous + current) %10
        total += current
        result_list2.append(current%10)
        if total %10 == 0 :
            if(total+current+previous)%10 ==1 :
                pisano = i+1
                break
    # if n < 60 then can grap from list, else have to mod 60 to get from list
    if n< 60:
        return (sum(result_list2[m:]))%10
    else:
        #n%(pisano+1)

print(fibonacci_partial_sum(1234,12345))

# start_time = time.time()
# print('answer is',fibonacci_total_naive(888888), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))

# start_time = time.time()
# print('answer is',fibonacci_total_efficient(888888), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))

# start_time = time.time()
# print('answer is',fibonacci_partial_sum(888888), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))

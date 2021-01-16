# Uses python3
import sys

def optimal_summands(n):
    # n is number of candy
    summands = []
    if n == 0:
        return 0
    elif n == [1]:
        return 1
    elif n == 2:
        return [2]
    total = 0
    i = 1
    stop = 0
    while total < n : #and stop == 0 :
        total += i
        if total >n:
            #stop =1
            break
        summands.append(i)
        i +=1
        remainder = n%total
    summands[-1] += remainder 

    return summands





# copy ma
def optimal_summands_copy(n):
    summands = []
    for i in range(1, n + 1):
        n -= i
        if n <= i:
            summands.append(n + i)
            break
        elif n == 0:
            summands.append(i)
            break
        else:
            summands.append(i)
    return summands

print(optimal_summands_copy(2))

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
#     summands = optimal_summands(n)
#     print(len(summands))
#     for x in summands:
#         print(x, end=' ')

# Uses python3

#%%

#%%
import sys
import itertools
def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

# print(partition3([3,3,3,3]))
# print(partition3([3,4,2]))
# print(partition3([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]))
#%%
def partition(A):
    total = sum(A)
    if total %3 != 0 or len(A) <3 :
        return 0
    # each set have to equal total //3
    answer = total //3
    

    return 'stop'

# print(partition([3,3,3,3]))
# print(partition([6,3,3,6]))
# print(partition([30]))
# print(partition([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]))

#%%
# for test
import numpy
def partitions(items):
    """ Finds if number of partitions having capacity W is >=3
    (int, int, list) -> (int) """
    
    total = sum(items)
    if total %3 != 0 or len(items) <3 :
        return 0
    n = len(items)
    W = sum(items) //  3
    count = 0 
    value = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            # print(value)
            if items[j-1]<=i:
                temp = value[i-items[j-1]][j-1] + items[j-1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == W: count += 1

    if count < 3:
        return 0
    else:
        return 1
# print(partitions([3,3,3,3]))
# print(partitions([3,4,2]))
# print(partitions([6,3,3,6]))
# print(partitions([30]))
# print(partitions([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]))

#%%
def partitions_copy(W, n, items):
    """ Finds if number of partitions having capacity W is >=3
    (int, int, list) -> (int) """
    count = 0 
    value = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if items[j-1]<=i:
                temp = value[i-items[j-1]][j-1] + items[j-1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == W: count += 1

    if count < 3: print('0')
    else: print('1')


#%%

if __name__ == '__main__':
    n = int(input())
    item_weights = [int(i) for i in input().split()]
    total_weight = sum(item_weights)
    if n<3: 
        print('0')
    elif total_weight%3 != 0: 
        print('0')
    else:
        partitions_copy(total_weight//3, n, item_weights)


# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


#%%
# W = max weight 10 and w is list of [item weight] weight = value
def max_gold_repeat(W,w): # can repeat
    value = [0] * (W+1)
    # value[0] = 0
    for W_i in range(1,W+1):
        # value[W_i]=0
        for i in w :
            if i<= W_i:
                tmp_val = value[W_i - i] + i
                if value[W_i] < tmp_val:
                    value[W_i] = tmp_val
    return value[W]

print(max_gold_repeat(10 ,[1, 4, 8]))

#%%
import numpy as np

def max_gold_not_repeat(W,w):
    # init two dimension array Note do not use [0] *2 as it will link each list
    value = [ [ 0 for _ in range(W+1) ] for _ in range(len(w)+1) ]
    for i in range(1,len(w)+1):
        for W_i in range(1,W+1):
            value[i][W_i] = value[i-1][W_i]       
            if w[i-1] <= W_i:
                tmp_val = value[i-1][W_i - w[i-1]] + w[i-1]
                if value[i][W_i] < tmp_val:
                    value[i][W_i] = tmp_val

    print(np.array(value)) 
    print(len(w),W-1)
    return value[len(w)][W]

print(max_gold_not_repeat(10 ,[1,4,8]))
print("\n" *3)
print(max_gold_not_repeat(10 ,[3,5,3,3,5]))
#%%
def optimal_weight_copyma(W, w):
    items = [0]
    for item in w:
        if item <= W:
            items.append(item)

    item_length = len(items)
    capacity = W + 1

    weights = [[0 for _ in range(item_length)] for _ in range(capacity)]

    for j in range(1, item_length):
        for i in range(1, capacity):
            previous = weights[i][j - 1]
            current = items[j] + weights[i - items[j]][j - 1]
            if current > i:
                weights[i][j] = previous
            else:
                weights[i][j] = max(previous, current)

    print(np.array(weights).transpose())
    print(len(w),W-1)
    return weights[-1][-1]
print(optimal_weight_copyma(10 ,[3,5,3,3,5]))


#%%
if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

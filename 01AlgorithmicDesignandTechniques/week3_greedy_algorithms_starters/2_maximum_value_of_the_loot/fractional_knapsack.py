# Uses python3
import sys

# input is capacity(int) and list of weigths with position same as list of values
def get_optimal_value(capacity, weights, values):
    # init list of value per KG
    ValuePerKg = [v / w for  v,w in zip(values,weights)  ]
    # sort desc weights and values according to ValuePerKg list
    weights_sorted = [x for _,x in sorted(zip(ValuePerKg,weights), reverse=True)]
    # values_sorted = [x for _,x in sorted(zip(ValuePerKg,values), reverse=True)]
    ValuePerKg_sorted = sorted(ValuePerKg,reverse=True)
    # after already sorted (most value/kg is leftmost), we get the left most item first
    n = len(weights)
    # initialize total value in bag
    value = 0
    for i in range(n):
        if capacity == 0:
            return(value)
        a = min(capacity,weights_sorted[i])
        value += a * (ValuePerKg_sorted[i])
        weights_sorted[i] -= a
        capacity -= a 
    return value


print(get_optimal_value(50,[20,50,30],[60,100,120]))
# print(get_optimal_value(10,[30],[500]))


# if __name__ == "__main__":
#     data = list(map(int, sys.stdin.read().split()))
#     n, capacity = data[0:2]
#     values = data[2:(2 * n + 2):2]
#     weights = data[3:(2 * n + 2):2]
#     opt_value = get_optimal_value(capacity, weights, values)
#     print("{:.10f}".format(opt_value))


# Psuedo code

# def Knapsack(W,w1,v1,...,w_n,v_n): # where W is capacity

#     # amount is place in knapsack
#     amount = [0] * (len(n))
#     totalValue = 0
#     repeat n times:
#         # W = 0 mean the knapsack is full then return total value
#         if W =0:
#             return (totalValue, amounts)
#         # set i = index of largest value/ kg
#         i = BestItem(W,w1,v1,...,w_n,v_n)
#         # compute how much to take of this item
#         # compare item weight (w_i) and space left in kanpsack(W). If item weight smaller mean can fit all then we take all
#         # if space in Knapsack is smaller then we take this item just to complete fill knapsack
#         a = min (w_i,W)
#         totalValue = totalValue + a *(vi/wi)
#         # update reamining quantity to 0 by minus a so we know that we already take this one to knapsack
#         wi = wi - a
#         # update place in knapsack of the amount we took in
#         # have to plus it self because 0.5 could come form other item
#         amount[i] = amount[i] + a
#         # update decrease the capacity
#         W = W-a
#     return (totalValue, amount)

    

# copy from internet. this better version sort only one time
def get_optimal_value(capacity, weights, values):
    value = 0.
    proportion = [float(v) / float(w) for v, w in zip(values, weights)]
    for _ in range(len(weights) + 1):
        if capacity == 0:
            return value
            break
        max_weight = max(proportion)
        index = proportion.index(max_weight)
        proportion[index] = -1
        add_capacity = min(capacity, weights[index])
        value += add_capacity * max_weight
        weights[index] -= add_capacity
        capacity -= add_capacity
    return value
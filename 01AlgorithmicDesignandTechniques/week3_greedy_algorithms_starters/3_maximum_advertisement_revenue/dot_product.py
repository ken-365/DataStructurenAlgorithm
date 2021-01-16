#Uses python3

import sys



# first step make a safe choice. Which is sort DESC first then pair and for product

def max_dot_product_naive(a, b):
    #write your code here
    a= sorted(a,reverse=True)
    b = sorted(b,reverse=True)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

print(max_dot_product_naive([1,3,-5],[-2,4,1]))



# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n = data[0]
#     a = data[1:(n + 1)]
#     b = data[(n + 1):]
#     print(max_dot_product(a, b))
    

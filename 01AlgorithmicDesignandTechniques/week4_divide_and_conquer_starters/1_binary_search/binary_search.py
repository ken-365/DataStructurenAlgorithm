# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1
    if a == 0:
        return 0
    while left <= right:
        # cal mid
        mid = left + (right-left)//2 
        if a[mid]  == x:
            return mid
        elif a[mid] < x:
            left = mid +1
        else :
            right = mid -1
    return -1
# print(binary_search([1158, 2755, 3364, 3716, 8503] ,47358))

def linear_search(a, x):
    if a == 0:
        return 0
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n = data[0]
#     m = data[n + 1]
#     a = data[1 : n + 1]
#     for x in data[n + 2:]:
#         # replace with the call to binary_search when implemented
#         print(binary_search(a, x), end = ' ')


from random import randint
def stress_test():
    
    while True:
        n = randint(0,50)
        k = randint(0,99999)
        alist = []
        for i in range(n):
            alist.append(randint(0,9999))
        alist = sorted(alist)
        if binary_search(alist,k) == linear_search(alist,k):
            print('OK')
        else:
            print(alist,k,binary_search(alist,k), linear_search(alist,k))
            return
        
    


print(stress_test())

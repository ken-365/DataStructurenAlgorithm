# Uses python3
import sys

def get_majority_element(a, left, right):
    # base case
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    alist = sorted(a) # if sorted here cannot do recursive
    n = right
    if n % 2 != 0:
        mid = n //2 
        if alist[mid] == alist[-1] or alist[mid] == alist[0]:
            return 1
    else:
        mid_plus_one = n //2
        if  alist[mid_plus_one] == alist[0]:
            return 1
        mid_minus_one = (n //2) -1
        if alist[mid_minus_one] == alist[-1] :
            return 1  
    return -1

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     if get_majority_element(a, 0, n) != -1:
#         print(1)
#     else:
#         print(0)

#copy internet
def get_majority_element2(a, left, right): # time use (0.11/10.0)
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    n = len(a)
    a.sort()
    if right % 2 == 0:
        major = n // 2 + 1
    if right % 2 != 0:
        major = (n + 1) // 2
    for i in range((n // 2) + (n % 2)):
        if a[i] == a[i + major - 1]:
            return 1
    return -1

#copy internet
def get_majority_element3(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    left_elem = get_majority_element3(a, left, (left + right - 1) // 2 + 1)
    right_elem = get_majority_element3(a, (left + right - 1) // 2 + 1, right)

    lcount = 0
    for i in range(left, right):
        if a[i] == left_elem:
            lcount += 1
    if lcount > (right - left) // 2:
        return left_elem

    rcount = 0
    for i in range(left, right):
        if a[i] == right_elem:
            rcount += 1
    if rcount > (right - left) // 2:
        return right_elem

    return -1

print(get_majority_element([1,1,1,1,3,5],0,6))
print(get_majority_element2([1,1,1,1,3,5],0,6))

from random import randint
def stress_test():
    n = randint(0,10000)
    alist = []
    for i in range(n):
        alist.append(randint(0,100))
    while True:
        if get_majority_element(alist,0,n) == get_majority_element2(alist,0,n):
            print('OK')
        else:
            print('Not ok')
            print(n,alist)
            print(get_majority_element(alist,0,n) , get_majority_element2(alist,0,n))
            return


# stress_test()
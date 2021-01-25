# Uses python3
import sys
import random

def partition3(a, l, r):
    pivot = a[l]
    m_1, m_2 = l ,l
    for i in range(l+1, r+1):
        if a[i] < pivot :
            a[i], a[m_1] = a[m_1], a[i]
            m_2 +=1
            a[i], a[m_2] = a[m_2], a[i]
            m_1 += 1 
        elif a[i] == pivot:
            m_2 +=1 
            a[i], a[m_2] = a[m_2], a[i]
    return m_1, m_2

def partition_copy(a, l, r):
    x = a[l]
    m1 = l
    m2 = l
    i = m1
    for i in range(l + 1, r + 1):
        if a[i] < x:
            a[i], a[m1] = a[m1], a[i]
            a[i], a[m2+1] = a[m2+1], a[i]
            m1 += 1
            m2 += 1
        elif a[i] == x:
            a[i], a[m2+1] = a[m2+1], a[i]
            m2 += 1
    return m1, m2

def partition2(a, l, r):
    pivot = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= pivot:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return 
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    #use partition3
    m_1,m_2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m_1 - 1)
    randomized_quick_sort(a, m_2 + 1, r)


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     randomized_quick_sort(a, 0, n - 1)
#     for x in a:
#         print(x, end=' ')

# test function
# alist = [3,5,3,3,1,8]
# l = 0
# r = len(alist) - 1
# randomized_quick_sort(alist,l,r)
# print(alist)

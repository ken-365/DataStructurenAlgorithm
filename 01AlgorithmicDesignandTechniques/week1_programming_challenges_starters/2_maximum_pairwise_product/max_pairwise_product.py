# Uses python3
# naive
# def naive(a):
#     # n = int(input())
#     # a = [int(x) for x in input().split()]
#     result = 0
#     for i in range( len(a)):
#         for j in range(i+1, len(a)):
#             if a[i]*a[j] > result and a[i] != a[j] :
#                 result = a[i]*a[j]
#     return result

# # print(naive([5,2,1]))

# # Fast algorithm
# def fast(A):
#     index1 = 1
#     for i in range(2,len(A)):
#         if A[i] > A[index1]:
#             index1 = i

#     if index1 == 0:
#         index2 = 1
#     else:
#         index2 = 0

#     for i in range(1,len(A)):
#         if i != index1 :
#             index2 = i

#     return(A[index1] * A[index2])

# print(fast([5,2,1]))










# # stress test
# from random import randint
# def stresstest(N,M):
#     while True:
#         n = randint(2,N)
#         A = [None] * (n)
#         for i in range(n):
#             A[i] = randint(1,M)
#         result1 = naive(A)
#         result2 = fast(A)
#         if result1 == result2:
#             print('OK')
#         else:
#             print(A)
#             print("Unmatch answer", result1,result2)
#             return

# stresstest(10,199999)

# for submission
import sys

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

a_sorted = sorted(a, reverse=True)

print(a_sorted[0]*a_sorted[1])

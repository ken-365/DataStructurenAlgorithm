# Uses python3
import sys

def merge(B,C,b):
    i = j = count_inverse = 0
    while i< len(B) and j < len(C):
        if B(i) <= C[j]:
            b.append(B(i))
            i+= 1
        else:
            b.append(C[j])
            j+=1
            count_inverse += 1
    b.append(B[i:])
    b.append(C[j:])
    return b, count_inverse

def get_number_of_inversions(a, b, left, right): # where a is an array and b is empty array
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    B = get_number_of_inversions(a, b, left, ave)
    C = get_number_of_inversions(a, b, ave+1, right)
    #write your code here
    sorted_array,count_inv = merge(B,C,b)
    return sorted_array

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     b = n * [0]
#     print(get_number_of_inversions(a, b, 0, len(a)))

print(get_number_of_inversions([2,3,9,2,9], [0,0,0,0,0], 0, 5))


def merge(left, right):
    i, j, inversion_counter = 0, 0, 0
    final = list()
    while i < len(left) and j< len(right):
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            inversion_counter += len(left) - i
            j += 1

    final += left[i:]
    final += right[j:]
        
    return final, inversion_counter

def mergesort(arr):
    global tot_count
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    sorted_arr, temp = merge(left, right)
    tot_count += temp

    return sorted_arr

# tot_count = 0
# n = int(input())
# seq = [int(i) for i in input().split()]
# mergesort(seq)
# print(tot_count)



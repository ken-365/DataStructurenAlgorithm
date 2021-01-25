# Uses python3
import sys
from itertools import chain
import timeit
import time
from random import randint

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    linelist = []
    for i in range(len(starts)):
        linelist.append((starts[i],'a_start')) 
        # indicate a_ prefix because incase we have same start, end and point. the linelist cansort by alphabet that always make start prior to point and prior to end 
    for i in range(len(ends)):
        linelist.append((ends[i],'c_end'))
    for i in range(len(points)):
        linelist.append(( points[i],'b_point',int(i) ))
    linelist.sort()
    
    count_segment = 0
    # start count
    for each in linelist:
        if each[1] == 'b_point':
            cnt[each[2]] =count_segment
        elif each[1] == 'a_start':
            count_segment += 1
        else:
            count_segment -= 1

    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

# [0 -> 5] and [7 -> 10]  // points are 1,6,11
print(fast_count_segments([0,7], [5,10],[1,6,11]))
print(fast_count_segments([0,-3,7], [5,2,10],[1,6]))
print(fast_count_segments([-10], [10],[-100,100,0]))


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n = data[0]
#     m = data[1]
#     starts = data[2:2 * n + 2:2]
#     ends   = data[3:2 * n + 2:2]
#     points = data[2 * n + 2:]
#     #use fast_count_segments
#     cnt = naive_count_segments(starts, ends, points)
#     for x in cnt:
#         print(x, end=' ')

def fast_count_segments_copy_from_internet(starts, ends, points):
    cnt = [0] * len(points)
    start_points = zip(starts, ['l'] * len(starts), range(len(starts)))
    end_points = zip(ends, ['r'] * len(ends), range(len(ends)))
    point_points = zip(points, ['p'] * len(points), range(len(points)))

    sort_list = chain(start_points, end_points, point_points)
    sort_list = sorted(sort_list, key=lambda a: (a[0], a[1]))
    segment = 0
    i = 0
    for num, letter, index in sort_list:
        if letter == 'l':
            segment += 1
        elif letter == 'r':
            segment -= 1
        else:
            cnt[index] = segment
            i += 1
    return cnt


def stress_test():
    n = randint(0,9)
    for 
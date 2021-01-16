# Uses python3
import sys
from collections import namedtuple
from operator import attrgetter
import time

Segment = namedtuple('Segment', 'start end')
# make a safe choice-> sort by end point and get end as each point if start of the next line < end of previous line skip else get its end as point

def optimal_points(segments):
    points = []
    #sort by end point of each line
    segments = sorted(segments, key=attrgetter('end') )
    # get end of the first line as point and if the next start point less than previous end point skip. else add its end point as points.
    for eachline in segments:
        if points == []:
            points.append(eachline.end)
        elif eachline.start > points[-1]:
            points.append(eachline.end)

    return points

def optimal_points_copy(segments):
    points = []
    segments = sorted(segments, key=attrgetter('end'))
    max_right = segments[0].end
    points.append(max_right)
    i = 1
    while i < len(segments):
        if max_right < segments[i].start:
            max_right = segments[i].end
            points.append(max_right)
        i += 1

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')


    


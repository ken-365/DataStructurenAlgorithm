#Uses python3

import sys

def IsGreaterorEqual(a,b):
    if b == -float('inf'):
        return True
    listofa = [int(x) for x in str(a) ]
    listofb = [int(x) for x in str(b) ]
    answer = True
    looping = True
    for i in listofa:
        for j in listofb:
            if i >j:
                answer = True
                looping = False
                break
            elif i< j:
                answer = False
                looping = False
                break
        if not looping:
            break

    return answer

# print(IsGreaterorEqual(3,41))
# print(IsGreaterorEqual(4445,4445))
# print(IsGreaterorEqual(45,43))

def largest_number(alist):
    answer = []
    while alist != []:
        maxDigit = -float('inf')
        for digit in alist:
            if IsGreaterorEqual(digit,maxDigit):
                maxDigit = digit
        answer.append(maxDigit)
        alist.remove(maxDigit)
    # answer = [str(x) for x in answer]
    # res = ""
    # for x in answer:
    #     res += x
    return answer #res
    
# copy ma
def IsGreaterOrEqual_2(digit, max_digit):
    return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))

def largest_number_copy(lst):
    answer = []
    
    while lst!=[]:
        max_digit = 0
        for digit in lst:
            if IsGreaterOrEqual_2(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        lst.remove(max_digit)

    return answer

print(largest_number_copy([1,2]))
print(largest_number([1,2]))

from random import randint
def stress_test():
    n = randint(0,299)
    test_list = [] 
    for i in range(n):
        test_list.append(randint(1,3000))
    i=1
    while True:
        if largest_number_copy(test_list) == largest_number(test_list):
            print('ok',i)
            i +=1
        else:
            print('Not ok', test_list,largest_number_copy(test_list) , largest_number(test_list))
    return 

print(stress_test())

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = input.split()
#     a = data[1:]
#     print(largest_number(a))
    

# Uses python3
import sys

#%%
def optimal_sequence(n): #  incorrect example given
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return sequence


print(optimal_sequence(11))

# input = sys.stdin.read()
# n = int(input)
# sequence = list(optimal_sequence(n))
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=' ')

# %%
def correct_sequence(n):

    # find the minimum operation of each number from 2 to n
    operlist = [float('inf')] *( n+1)
    operlist[0]= 0
    operlist[1]= 0
    
    for i in range(2, n+1):
        res1 = res2 = res3 = float('inf')
        if i %2 == 0:
            res1 = operlist[i // 2]
        if i %3 == 0:
            res1 = operlist[i // 3] 
        
        res3 = operlist[i-1]
        min_oper = min(res1,res2,res3)
        
        operlist[i] = min_oper  +1
    
    # create result list
    resultlist = [n]
    while n > 1:
        res4 = res5 = res6 = float('inf')
        tmplist = []
        if n %2 == 0 and operlist[n] -1 == operlist[n // 2]:
            n = n // 2
        elif n %3 == 0 and operlist[n] -1 == operlist[n // 3]:
            n = n // 3
        else:
            n = n-1
            
        resultlist.append(n)
    return resultlist
        
print(correct_sequence(96234))


# %%

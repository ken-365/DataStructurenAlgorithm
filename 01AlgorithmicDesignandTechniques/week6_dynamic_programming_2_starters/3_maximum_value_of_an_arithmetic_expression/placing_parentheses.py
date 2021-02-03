
#%%
## Uses python3
import numpy as np
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(M,m,i,j,op): 
    # where i is start index and j is end index 
    min_value =   float('inf')
    max_value = - float('inf')
    for k in range(i,j):
        a = evalt(M[i,k],M[k+1,j],op[k])
        b = evalt(m[i,k],m[k+1,j],op[k])
        c = evalt(M[i,k],m[k+1,j],op[k])
        d = evalt(m[i,k],M[k+1,j],op[k])
        min_value = min(min_value,a,b,c,d)
        max_value = max(max_value,a,b,c,d)
    return min_value, max_value

def get_maximum_value(dataset):
    number = []
    operator =[]
    for i in dataset:
        if i  in ['+', '-', '*']:
            operator.append(i)
        else:
            number.append(i)
        

    #init 2D numpy array
    n = len(number)
    M = np.zeros((n,n))
    m = np.zeros((n,n))
    # fill in first diaganal
    for i in range(len(number)):
        m[i,i] =number[i]
        M[i,i] =number[i]
    # start fill
    for s in range(1,n):
        for i in range(0,n-s):
            # print(M)
            # print(m)
            j = i + s
            m[i,j] , M[i,j] = MinAndMax(M,m,i,j,operator)
            
  
    return int(M[0][n-1])

# print(get_maximum_value("1+5"))

# print(get_maximum_value('5-8+7*4-8+9'))
if __name__ == "__main__":
    print(get_maximum_value(input()))

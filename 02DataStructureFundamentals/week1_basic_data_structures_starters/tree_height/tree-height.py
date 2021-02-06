# python3
#%%
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;        
def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()


#%%
class TreeHeight:
        def read(self,n,parent):
                self.n = n
                self.parent = parent

        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;   
        

tree = TreeHeight()
tree.read(5,[4 ,-1 ,4 ,1 ,1])
print(tree.compute_height())        
#%%
class TreeHeight:
        def read(self,n,parent):
                self.n = n
                self.parent = parent
                self.root = 0
                self.nodes = [None] * n 
                for i in range(self.n):
                        if self.parent[i] == -1:
                                self.root = i
                                break
                
                for i in range(self.n):
                        if self.parent[i]  == -1:
                                self.root = i
                        else:
                                if  self.nodes[self.parent[i]] != None :
                                        self.nodes[self.parent[i]].append(i)
                                else:
                                        self.nodes[self.parent[i]] = [i]
               
        def dept(self):
                
        def compute_height(self):
                # Replace this code with a faster implementation
                if this node == None:
                        return 0
                return 1+ max(compute_height(self.nodes))


tree = TreeHeight()
tree.read(5,[4 ,-1 ,4 ,1 ,1])
print(tree.compute_height())  
# %%
class TreeHeight_copy:
    def __init__(self):
        self.n = 0
        self.parent = []
        self.cache = []

    def read(self,n,parent):
        self.n = n
        self.parent = parent
        self.cache = [0] * self.n

    def depth_len(self, node_id):
        parent = self.parent[node_id]
        if parent == -1:
            return 1

        if self.cache[node_id]:
            return self.cache[node_id]

        self.cache[node_id] = 1 + self.depth_len(self.parent[node_id])
        return self.cache[node_id]

    def compute_height(self):
        return max([self.depth_len(i) for i in range(self.n)])

tree = TreeHeight_copy()
tree.read(5,[4 ,-1 ,4 ,1 ,1])
print(tree.compute_height())  

#%% for testing
import time , random

def romanToInt(s: str) -> int:
        # init 
        adict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        answer = 0
        #split
        for i,alphabet in enumerate(list(s)):
                if i+1 != len(list(s)):
                        if list(s)[i] == 'I' and (list(s)[i+1] in {'V','X'} ) \
                                or (list(s)[i] == 'X' and (list(s)[i+1] in {'L','C'} )) \
                                        or (list(s)[i] == 'C' and (list(s)[i+1] in {'D','M'})) :
                                answer -= adict[alphabet]
                        else:answer += adict[alphabet]
                else:
                        answer += adict[alphabet]
        return answer

def romanToInt_copy1( s: str) -> int:
        x = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        k = list(x.keys())
        sum = 0
        com = False
        for idx, i in enumerate(s):
            if com:
                if k.index(i) > k.index(com):
                    sum -= 2*x[com]
            sum += x[i]
            com = i
        return(sum)


def romanToInt_copy( s: str) -> int:
        lookup = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans = 0
        previousVal = -1
        for i in range(len(s)):
                currentVal = lookup[s[len(s)-1-i]]
                if previousVal > currentVal: 
                        currentVal *= -1
                ans = ans + currentVal
                previousVal = currentVal
        return ans

def romanToInt2(s):
        adicts = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
  
        for i in range(len(list(s))):
                if adicts[list(s)[i]] < 20:
                        tmp = adicts[list(s)[i]] *-1
                else:
                        tmp = adicts[list(s)[i]]
                ans += tmp
    
        return ans
# print(romanToInt("IX"), romanToInt("IX") == 9) 
# print(romanToInt("IV"), romanToInt("IV") == 4)
# print(romanToInt("LVIII"),romanToInt("LVIII") == 58)

adicts = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
s = list(adicts.keys())
tmp = []
for i in range(15000):
       tmp.append(random.choice(s)) 
tmp = "".join(tmp)

start = time.time()
romanToInt(tmp)
end = time.time()
print(end - start)

start = time.time()
romanToInt_copy1(tmp)
end = time.time()
print(end - start)

start = time.time()
romanToInt_copy(tmp)
end = time.time()
print(end - start)

start = time.time()
romanToInt2(tmp)
end = time.time()
print(end - start)

# %%

def isPalindrome( x: int) -> bool:
        # case where x<10 is not palindome
        if x < 10:
            return False
        reverted = 0
        if x % 10 == 0:
            return False
        
        while x  > reverted:
               reverted = reverted*10 +  x % 10 
               x = x//10
        print(x, reverted)
        return x== reverted or x == reverted //10
               
               
print(isPalindrome(5115))        
print(isPalindrome(121))
print(isPalindrome(845))
print(isPalindrome(65456))
print(isPalindrome(30))
# %%
def isMatch(left,right):
        if left == '(' and right == ')':
            return True
        if left == '[' and right == ']':
            return True
        if left == '{' and right == '}':
            return True
        return False
        
def isValid( s: str) -> bool:
        inverse = { ")":"(","]":"[","}":"{" }
        close_set = { ")","]","}"}
        stack = []
        for letter in s:
            if letter in close_set:
                if not stack: return False
                if stack[-1] != inverse[letter]: return False
                stack.pop()
            else:
                stack.append(letter)
        if stack: return False
        return True

print(isValid("(){}}{"))
# print(isValid("{[]}"))
# print(isValid("([)]"))
# print(isValid("{"))

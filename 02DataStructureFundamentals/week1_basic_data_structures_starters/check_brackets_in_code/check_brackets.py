# python3

from _typeshed import OpenBinaryModeReading
import sys
#%%
class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False
    
def bracket_check(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            #stack.Push(next)
            opening_brackets_stack.append(Bracket(next,i))

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            #check if stack is empty return false
            if len(opening_brackets_stack) == 0:
                return(i)
            top = opening_brackets_stack.pop()            
            if not top.Match(next):
                return(i+1)
                            
    if len(opening_brackets_stack) != 0:
        # print(opening_brackets_stack.pop().brak)
        return(opening_brackets_stack.pop().position +1 )  
    else:
        return 'Success'

# print(bracket_check("{}[]"))
# print(bracket_check("[()]"))
# print(bracket_check("{[]}()"))
# print(bracket_check("{"))
# print(bracket_check("{[}"))
# print(bracket_check("foo(bar);"))
# print(bracket_check("foo(bar[i);"))
# All test case pass

# stress test with copy code
class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def bracket_check_copy(text):
    opening_brackets_stack = []
    for index, next in enumerate(text, start=1):
        if next in ("[", "(", "{"):
            opening_brackets_stack.append(Bracket(next, index))

        elif next in ("]", ")", "}"):
            if not opening_brackets_stack:
                return index

            top = opening_brackets_stack.pop()
            if not top.match(next):
                return index
    if opening_brackets_stack:
        top = opening_brackets_stack.pop()
        return top.position

    return "Success"


    
#%%

if __name__ == "__main__":
    text = sys.stdin.read().strip("\n")
    print(bracket_check(text))

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            #stack.Push(next)
            opening_brackets_stack.append(Bracket(next,i))

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            #check if stack is empty return false
            if len(opening_brackets_stack) == 0:
                print('empty list')
            top = opening_brackets_stack.pop()
            if  nottop.Match(next):
                print("fail",i,top.bracket_type,next)
            else:
                print('match')
        
    # Printing answer, write your code here
#%%

# %%

# %%

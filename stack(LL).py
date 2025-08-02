class Node:
    def __init__(self,value):
        self.data = value 
        self.next = None 

    
class Stack:
    def __init__(self):
        self.top = None 

    def isEmpty(self):
        return self.top == None 
    
    def push(self,value):
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node 

    def peek(self):
        if (self.isEmpty()):
            return "Stack Empty"
        else:
            return self.top.data
        
    def pop(self):
        if (self.isEmpty()):
            return "Stack Empty"
        else: 
            data = self.top.data
            self.top = self.top.next 
            return data 
            
    def size(self):
        temp = self.top 
        count = 0 
        while temp is not None:
            temp = temp.next
            count += 1

        return count

    def traverse(self):

        temp = self.top 
        while temp != None:
            print(temp.data)
            temp = temp.next 

def reverse_string(text):
    s = Stack()
    for i in text: 
        s.push(i)
    res = "" 
    while (not s.isEmpty()):
        res += s.pop() 

    print(res) 

def text_editor(text, pattern):
    u = Stack() 
    r = Stack()

    for i in text: 
        u.push(i)

    for i in pattern: 
        if i == 'u':
            data = u.pop()
            r.push(data)
        else:
            data = r.pop() 
            u.push(data)

    res = ""
    while (not u.isEmpty()):
        res = u.pop() + res 
    print(res) 

# Celebrity Problem 
def find_the_celeb(L):
    s = Stack()

    for i in range(len(L)):
        s.push(i)

    while s.size() >= 2:
        i = s.pop() 
        j = s.pop() 
        if L[i][j] == 0:
            # j is not a celebrity 
            s.push(i)
        else:
            # i is not a celebrity 
            s.push(j)
    celeb = s.pop() 
    for i in range(len(L)):
        if i != celeb:
            if L[i][celeb] == 0 or L[celeb][i] == 1:
                print("No one is a celebrity")
                return
            
    print("The celebrity is",celeb)

# Balanced Bracket Problem 
def bracket(s):
    s = Stack() 
    mapping = {')':'(','}':'{',']':'['}

    open_brackets= set(mapping.values())
    close_brackets = set(mapping.keys())

    for char in s:
        if char in open_brackets:
            s.push(char)
        elif char in close_brackets:
            if s.isEmpty():
                return False
            top_element = s.pop()
            if mapping[char] != top_element:
                return False 
            
    return s.isEmpty()


# --- Test Cases ---
print(f"'()' is valid: {bracket('()')}")             # Expected: True
print(f"'()[]{{}}' is valid: {bracket('()[]{}')}")     # Expected: True
print(f"'{{[()]}}' is valid: {bracket('{[()]}}')}")    # Expected: True
print(f"'([)]' is valid: {bracket('([)]')}")           # Expected: False
print(f"'(((' is valid: {bracket('(((')}")            # Expected: False
print(f"'{{[' is valid: {bracket('{[')}")              # Expected: False
print(f"']' is valid: {bracket(']')}")                # Expected: False
print(f"'' is valid: {bracket('')}")                  # Expected: True
print(f"'(]' is valid: {bracket('(]')}")             # Expected: False
print(f"'{{}}[]' is valid: {bracket('{}[]')}")         # Expected: True
print(f"'{{{{' is valid: {bracket('{{{{')}")  
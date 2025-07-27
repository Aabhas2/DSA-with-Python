# Linked List 
class Node: 
    def __init__(self,value):
        self.data = value
        self.next = None 

class LinkedList:
    def __init__(self):
        # Empty Linked List 
        self.head = None 
        self.n = 0 #number of nodes in linked list 

    def __len__(self):
        return self.n
 
    def __str__(self):
        curr = self.head
        result = ''

        while curr != None: 
            result += str(curr.data) + '->'
            curr = curr.next 
        return result[:-2]
    
    def insert_head(self,value):
        # create new node 
        new_node = Node(value)
        # create connection 
        new_node.next = self.head 
        self.head = new_node
        self.n += 1  

    def append(self,value): # insert tail  
        if self.head == None: 
            # empty 
            self.head = new_node 
            self.n += 1
            return 

        new_node = Node(value) 
        curr = self.head
        while curr.next != None:
            curr = curr.next 

        # at the last node 
        curr.next = new_node 
        self.n += 1
        
    
    def insert_after(self,pos,value):
        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == pos:
                break 
            curr = curr.next 

        if curr != None:
            new_node.next = curr.next 
            curr.next = new_node 
            self.n += 1
        else:
            return 'Item Not Found'
    def clear(self):
        self.head = None 
        self.n = 0

    def delete_head(self):
        if self.head == None: 
            # empty list 
            return 'Empty LL'
        self.head = self.head.next
        self.n -= 1  

    def pop(self):
        if self.head == None:
            return 'Empty LL'

        curr = self.head

        if curr.next == None:
            return self.delete_head()
            

        while curr.next.next != None: 
            curr = curr.next 
        
        # curr - 2nd last node 
        curr.next = None 
        self.n -= 1 

    def remove(self,value):
        curr = self.head 
        if curr == None: 
            return 'Empty Linked List'

        if curr.data == value: 
            return self.delete_head()
            

        while curr.next != None:
            if curr.next.data == value:
                break 
            curr = curr.next
        # 2 cases 

        if curr.next  == None:
            return "Item Not Found"
        else:
            curr.next = curr.next.next
        
    def search(self,item):
        curr = self.head 
        pos = 0 
        while curr != None:
            if curr.data == item:
                return pos 
            curr = curr.next 
            pos += 1 
        return 'Item Not Found'

    def __getitem__(self,index):
        curr = self.head 
        pos = 0 

        while curr != None: 
            if pos == index: 
                return curr.data 
            curr = curr.next 
            pos += 1
        return 'IndexError'

    def replace_max(self,value):
        temp = self.head 
        max = temp

        while temp != None:
            if temp.data > max.data:
                max = temp
            temp = temp.next 
        
        max.data = value 

    def sum_odd_nodes(self):
        temp = self.head 
        count = 0 
        result = 0
        
        while temp != None:
            if count % 2 != 0:
                result = result + temp.data
            count += 1
            temp = temp.next 

        print(result)

    def reverse_int(self):
        prev_node = None 
        curr_node = self.head

        while curr_node != None: 
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node 
            curr_node = next_node 

        self.head = prev_node


word = LinkedList()
word.insert_head("T")
# word.insert_after("h")
# word.insert_after("e")
# word.insert_after("/")
# word.insert_after("*")
# word.insert_after("s")
# word.insert_after("k")
# word.insert_after("y")
# word.insert_after("*")
# word.insert_after("i")
# word.insert_after("s")
# word.insert_after("/")
# word.insert_after("/")
# word.insert_after("b")
# word.insert_after("l")
# word.insert_after("u")
# word.insert_after("e")

print(word)
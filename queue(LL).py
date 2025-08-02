class Node: 
    def __init__(self,value):
        self.data = value 
        self.next = None 

class Queue:
    def __init__(self):
        self.front = None 
        self.rear = None 

    def enqueue(self,value):
        new_node = Node(value)

        if self.front == None:
            self.front = new_node 
            self.rear = new_node
        else:
            self.rear.next = new_node 
            self.rear = new_node 

    def dequeue(self):
        if self.front == None: 
            return "Empty"
        else:
            self.front = self.front.next

    def isEmpty(self):
        return self.front == None
            
    def size(self):
        temp = self.front 
        count = 0 

        while temp != None:
            count += 1 
            temp = temp.next 
        return count
    
    def front_item(self):
        if self.isEmpty():
            return 'Empty'
        else:
            return self.front.data 
        
    def rear_item(self):
        if self.isEmpty():
            return "Empty"
        else:
            return self.rear.data 

    def traverse(self):
        temp = self.front 

        while temp != None: 
            print(temp.data)
            temp = temp.next 

q = Queue() 
q.enqueue(2)
q.enqueue(34)
q.enqueue(10)
q.enqueue(1)
q.enqueue(12)

q.traverse() 

# print("\n")
# q.dequeue() 
# q.traverse() 
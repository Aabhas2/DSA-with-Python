# Dynamic Array 

import ctypes

class MyList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # create C type array with size = self.size 
        self.A = self.create_array(self.size)

    def __len__(self):
        return self.n
    
    def __str__(self):
        # e.g [1,2,3]
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' + result[:-1] + ']'
    
    def __getitem__(self,index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'

    def __delitem__(self,pos):
        if 0<= pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]

            self.n -= 1
            

    def append(self,item):
        if self.n == self.size: 
            # resize 
            self.__resize(self.size*2)
        # append 
        self.A[self.n] = item
        self.n += 1

    def pop(self):
        if self.n == 0:
            return 'Empty list'
        
        print(self.A[self.n-1])
        self.n -= 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self,key):
        for i in range(self.n):
            if self.A[i] == key:
                return i
            
        return 'ValueError - not found in list'

    def insert(self,pos,item):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item 
        self.n += 1

    def remove(self,item):
        pos = self.find(item)
        if type(pos) == int:
            # delete 
            self.__delitem__(pos)

        else: 
            return pos

    def __resize(self,new_capacity):
        # create a new array with new capacity 
        B = self.create_array(new_capacity)
        self.size = new_capacity
        #copy elements of A to B 
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A 
        self.A = B 

    def create_array(self,capacity):
        # creates a C type array(static,referential) with size capacity
        return (capacity*ctypes.py_object)()
    
L = MyList()
L.append('hello')
L.append(3.4)
L.append(True)
L.append(100)
print(L)
L.insert(0,0)
print(L)
L.insert(2,234050105)
print(L)
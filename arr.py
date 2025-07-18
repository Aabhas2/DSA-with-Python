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

    def append(self,item):
        if self.n == self.size: 
            # resize 
            self.__resize(self.size*2)
        # append 
        self.A[self.n] = item
        self.n += 1

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

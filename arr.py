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
        if isinstance(index, int):
            if index < 0:
                index = self.n + index 
            if 0 <= index < self.n:
                return self.A[index]
            else:
                raise IndexError("Index out of range")
            
        elif isinstance(index, slice):
            return self._handle_slice(index)
        else:
            raise TypeError("List indexes must be integers or slices, not" + type(index).__name__)

    def __delitem__(self,pos):
        if pos < 0:
            pos = self.n + pos 

        if 0 <= pos < self.n: 
            for i in range(pos,self.n - 1):
                self.A[i] = self.A[i+1]
            self.n -= 1
        else:
            raise IndexError("Index out of range for deletion")
            
    def sort(self):
        if self.n <= 1:
            return 
        
        for i in range(self.n - 1):
            min_index = i
            for j in range(i+1,self.n):
                if self.A[j] < self.A[min_index]:
                    min_index = j 
            self.A[i], self.A[min_index] = self.A[min_index], self.A[i]

    def min(self):
        if self.n == 0:
            raise ValueError("min() arg is an empty sequence.")
        min_val = self.A[0]
        for i in range(1,self.n):
            if self.A[i] < min_val:
                min_val = self.A[i]

        return min_val
    
    def max(self):
        if self.n == 0:
            raise ValueError("max() arg is an empty sequence.")
        max_val = self.A[0]
        for i in range(1,self.n):
            if self.A[i] > max_val:
                max_val = self.A[i]

        return max_val
    
    def sum(self):
        if self.n == 0:
            raise ValueError("List is empty.")
        total = 0 
        for i in range(self.n):
            total += self.A[i]

        return total

    def append(self,item):
        if self.n == self.size: 
            # resize 
            self.__resize(self.size*2)
        # append 
        self.A[self.n] = item
        self.n += 1

    def extend(self,item):
        for i in item: 
            self.append(i)

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
L.append(3.4)
L.append(100)
L.append(1)
L.append(23)
L.append(7)
print(L)
L.sort()
print(L)
print(L.max())
print(L.min())
print("SUM: ",L.sum())
P = ('2,3,4,5,6','hellooo')
L.extend(P)
print(L)
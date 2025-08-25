# Linear Search | Time complexity: O(n) , No sorting required 
# Brute Force 

def linear_search(arr,item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1    

# Binary Search | works only on sorted array 
def binary_search(arr,low,high,item):
    if low <= high: 
        # search 
        mid = (low + high) // 2 
        if arr[mid] == item: 
            return mid 
        elif arr[mid] > item: 
            return binary_search(arr,low,mid-1,item)
        else: 
            return binary_search(arr,mid+1,high,item)
    else: 
        return -1 
    
# Sorting 
def is_sorted(arr): 
    sorted = True 
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            sorted = False

    return sorted 

# Monkey sort
import random  
import time 
def monkey_sort(arr):
    while not is_sorted(arr):
        time.sleep(1)
        random.shuffle(arr)
        print(arr)
    print(arr)

# Bubble sort | time complexity: O(N^2)
def bubble_sort(arr): 
    for i in range(len(arr) - 1):
        flag = 0 
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag += 1
        if flag == 0: 
            break
    print(arr)

# Selection Sort | O(N^2)
def selection_sort(arr):
    for i in range(len(arr) - 1):
        print(i+1, "pass",end=" ")
        min = i 

        print("Current min is ",arr[min])
        for j in range(i+1,len(arr)):
            print("Current item under observation",arr[j])
            if arr[j] < arr[min]:
                print("Current item is less than min")
                min = j
                print("Now the min has become",arr[min])
        arr[i], arr[min] = arr[min], arr[i]
        print(arr)
        print('-'*50)
    print(arr)
#  Selection sort is faster than bubble sort 
# Selection sort is not adaptive but bubble sort is 
# same way selection sort is not stable but bubble sort is 

# Merge Sort 
# merge_sorted is a helper function 
def merge_sorted(arr1,arr2):  
    i = j = 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
    while i < len(arr1):
        merged.append(arr1[i])
        i+=1

    while j < len(arr2):
        merged.append(arr2[j])
        j+=1

    return merged

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = mrrge

a = [23,14,11,67,45,61]
selection_sort(a)

#!/usr/bin/env python
# coding: utf-8

# # Dynamic Array Exercise
# ____
#
# In this exercise we will create our own Dynamic Array class!
#

import array as array


class DynamicArray(object):
    '''
    DYNAMIC ARRAY CLASS (Similar to Python List)
    '''
    def __init__(self,data_type,first_value):
        self.n = 1  # Count actual elements (Default is 0)
        self.capacity = 1  # Default Capacity
        self.data_type = data_type
        self.A = array.array(self.data_type,[first_value])

    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.n

    def __getitem__(self, k):
        """
        Return element at index k
        """
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds!')  # Check it k index is in bounds of array

        return self.A[k]  # Retrieve from array at index k


    def append(self, ele):
        """
        Add element to end of the array
        """
        self.capacity += 1
        self._resize(self.capacity)

        self.A[self.capacity-1] = ele
        self.n += 1

    def _resize(self, new_cap):
        """
        Resize internal array to capacity new_cap
        """
        B = self.make_array(new_cap)  # New bigger array

        for k in range(self.n):  # Reference all existing values
            B[k] = self.A[k]

        self.A = B  # Call A the new bigger array
        self.capacity = new_cap  # Reset the capacity

    def make_array(self, new_cap):
        """
        Returns a new array with new_cap capacity
        """
        new_array = array.array(self.data_type,[0]*new_cap)
        print(new_array[0])
        return new_array


# Instantiate
arr = DynamicArray('i',4)

print("Inital Array Length: ",len(arr))
# Append new element

arr.append(1)

arr.append(2)

print('Printing items by index:')
for i in range(0,len(arr)):
    print(arr[i])

print("Final Array Length: ",len(arr))

# Awesome, we made our own dynamic array! Play around with it and see how it auto-resizes. Try using the same **sys.getsizeof()** function we worked with previously!

# # Great Job!

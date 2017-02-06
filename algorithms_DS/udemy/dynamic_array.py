#!/bin/env python3

import sys
import ctypes
from random import sample

class DefaultList(object):

    def __init__(self):
        self.n = 10
        self.data = []
        
    def show(self):
        for i in range(self.n):
            a = len(self.data)
            b = sys.getsizeof(self.data)
            print('Length: {0:3d}; Size in bytes: {1:4d} '.format(a,b))
            self.data.append(self.n)
        print("Arr: ", self.data)
        
class DynamicArray(object):
    '''
    illustrates implementation of Python Lists
    '''
    def __init__(self):
        """
        capacity is extent of growth of our array.
        Once reached, the array doubles in size so 
        as to accomodate append() calls in future.
        """
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        return number of elements sorted in array
        """
        return self.n
        
    def __getitem__(self, k):
        """
        return element at index k
        """
        if not 0 <= k <= self.n:
            if k != -1:
                return IndexError('K is out of bounds!')
            else:
                return self.A[self.n-1]
        return self.A[k]
    
    def _resize(self, new_cap):
        B = self.make_array(new_cap) # bigger array of new size
        for k in range(self.n): # reference existing values
            B[k] = self.A[k]

        self.A = B # A is the bigger array now
        # del B
        self.capacity = new_cap
        
    def append(self, ele):
        if self.n == self.capacity: # length of array reached capacity
            # worst case amortized analysis, O(n)
            self._resize(2*self.capacity)
        # else, O(1)
        
        self.A[self.n] = ele # self.n being the new index, since it's 0 indexed
        self.n += 1 # update array length
        
    def extend(self, ele_list):
        m = len(ele_list)
        # import pdb; pdb.set_trace()
        if self.n+m >= self.capacity:
            self._resize(2*self.capacity+m)

        for ix, ele in enumerate(ele_list):
            self.A[self.n+ix] = ele
        self.n += m
        
    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

if __name__ == '__main__':
    print("\nusing inbuilt list [] ....\n")
    DefaultList().show()
    
    print("""\n...........and now:
    using ctypes.py_object for a custom DynamicArray
    """)
    
    arr = DynamicArray()
    arr.append(1)
    print('Length: {0:3d}; Size in bytes: {1:4d}; New capacity: {2:3d}'\
          .format(len(arr), sys.getsizeof(arr), arr.capacity))
    arr.append(2)
    print('Length: {0:3d}; Size in bytes: {1:4d}; New capacity: {2:3d}'\
          .format(len(arr), sys.getsizeof(arr), arr.capacity))

    print("Arr: ",list(arr))
    print("\tlist(arr) succeeded\n")
    arr.append("aaa")
    print('Length: {0:3d}; Size in bytes: {1:4d}; New capacity: {2:3d}'\
          .format(len(arr), sys.getsizeof(arr), arr.capacity))

    try:
        print("Arr: ",list(arr))
    except ValueError as e:
        print("\nERROR while executing list(arr) - ValueError: %s" % e)
        print("falling back to manual access index by index, one at a time..")
        print("Arr: [%s,%s,%s]" %
              (arr[0],arr[1], arr[2]))
    
    print("""
    # at this point, list(arr) fails. This is probably because 
    capacity exceeds length. And so, it seems ctypes.py_object 
    wouldn't comply with list() anymore. 

    Perhaps, we need to read more about how ctypes work by RTFM'g the damn thing.
    """)

    x = sample(range(1,100),60)
    print("extending arr to add:\n %s\n of length %s..using a custom extend() method" % (x,len(x)))
    arr.extend(x)
    print('Total new Length: {0:3d}; Size in bytes: {1:4d}; New capacity: {2:3d}'\
          .format(len(arr), sys.getsizeof(arr), arr.capacity))
    # print("Arr: ",list(arr))
    y = sample(range(1,50),20)
    print("extending arr to add:\n %s\n of length %s..using a custom extend() method" % (y,len(y)))
    arr.extend(y)
    print('Total new Length: {0:3d}; Size in bytes: {1:4d}; New capacity: {2:3d}'\
          .format(len(arr), sys.getsizeof(arr), arr.capacity))
    print("Arr: [%s,%s,%s,%s,%s,...,%s,...%s] and so on.." %
          (arr[0],arr[1], arr[2], arr[3], arr[4],arr[50], arr[-1]))

# questions:
# (refer to output in file: dynamic_array.output in this directory)
# 1. why is the size of DynamicArray constant at 56
# 2. precise explanation of list(arr) failure?
# 3. in _resize, I've commented out 'del B'. Should I have not?
#    I have not seen any effect on the result, but is the memory
#    usage affected? or does GC take care of this?

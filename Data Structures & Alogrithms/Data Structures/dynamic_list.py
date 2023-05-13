"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/

Reference:
https://github.com/campusx-official/dsa-using-python
"""
import ctypes


class IndexError(BaseException):
    """Raise exception on Stack Overflow.
    """
    print("Index Error - Index out of Range.")

class DynamicList:
    """
    create python list without using List.
    """

    def __init__(self) -> None:
        """Init...
        """
        self._size = 1 # Total size of the array.
        self._n_items = 0 # no. of elements in array.

        # Create array with size = self.size
        self._arr = self._make_array()
    
    def __len__(self):
        """Get the length of the array.
        """
        return self._n_items
    
    def __str__(self):
        """String function of the class.
        """
        result = '['
        for i in range(self._n_items):
            result = result + str(self._arr[i]) + ',' if i==self._n_items-1 else ''
        return result + ']'
    
    def __getitem__(self,index):
        if 0<=index<self._n_items:
            return self._arr[index]
        else:
            raise IndexError

    def __append__(self, val):
        """Append the val into array.
        """
        if self._size == self._n_items: # Resize the array.
            self._resize()
        else: # Append the val.
            self._arr[self._n_items] = val
            self._n_items += 1
    
    def pop(self):
        if self._n_items > 0:
            self._n_items -= 1
            return self._arr[self._n_items+1]
        else:
            raise IndexError


    # PRIVATE FUNCTIONS
    def _make_array(self):
        # Create array with defined size.
        return (self._size*ctypes.py_object)()
    
    def _resize(self):
        temp = (2*self._size*ctypes.py_object)()
        for i in range(self._n_items):
            temp[i] = self._arr[i]
        self._arr, self._size = temp, self._size*2

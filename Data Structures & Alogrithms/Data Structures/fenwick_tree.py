"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/

Reference:
https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/fenwick_tree.py
"""

class FenwickTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.bit_tree = [0]*self.n
        for i in range(n):
            self.bit_tree[i] = arr[i]
        self.build()

    def build(self): 
        n = self.n
        for i in range(n):
            j = i + (i & -i) 
            if j < n:
                self.bit_tree[j] += self.bit_tree[i]
    
    def update(self, ind, val):
        n = self.n
        while ind <= n:
            self.bit_tree[i] += val
            i = i + (i & -i)



if __name__ == "__main__":
    import doctest

    doctest.testmod()
"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/

Reference:
https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/fenwick_tree.py
"""

from typing import List

class FenwickTree:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.bit_tree = [0]*self.n
        for i in range(self.n):
            self.bit_tree[i] = arr[i]
        self.build()
    
    @staticmethod
    def next_(index: int) -> int:
        return index + (index & (-index))
    
    @staticmethod
    def prev(index: int) -> int:
        return index - (index & (-index))

    def build(self):
        n = self.n
        for i in range(n):
            j = self.next_(i)
            if j < n:
                self.bit_tree[j] += self.bit_tree[i]

    def update(self, ind: int, val: int) -> None:
        n = self.n
        while ind <= n:
            self.bit_tree[ind] += val
            ind = self.next_(ind)
    
    def prefix(self, right: int) -> int:
        result = 0
        while right >= 0:
            result += self.bit_tree[right]
            right = self.prev(right)
        return result

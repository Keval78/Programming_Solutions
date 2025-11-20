'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from collections import defaultdict

# Implementing Segment Tree...
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.seg_tree = [0]*(self.n*2)
        self.build()

    def build(self):
        n = self.n
        for i in range(n-1, 0, -1):
            self.seg_tree[i] = max(self.seg_tree[i<<1], self.seg_tree[i<<1|1])

    def update(self, i, val):
        i = i + self.n
        self.seg_tree[i] = val
        
        while i > 1:
            self.seg_tree[i>>1] = max(self.seg_tree[i], self.seg_tree[i^1])
            i >>= 1
    
    def find(self, val):
        idx = 1
        if self.seg_tree[idx] < val:
            return -1
        while idx < self.n:
            if (idx<<1 < 2*self.n) and self.seg_tree[idx<<1] >= val:
                idx = idx<<1
            elif (idx<<1|1 < 2*self.n) and self.seg_tree[idx<<1|1] >= val:
                idx = idx<<1|1
        return idx-self.n

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        seg = SegmentTree(len(baskets))
        for i, basket in enumerate(baskets):
            seg.update(i, basket)
        left_fruit = len(fruits)
        for fruit in fruits:
            idx = seg.find(fruit)
            if idx != -1:
                left_fruit -= 1
                seg.update(idx, -1)
        return left_fruit


    def numOfUnplacedFruits2(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)

        # sqrt decomposition
        bucket_sz = int(ceil(sqrt(n)))
        buckets = [0] * bucket_sz

        for i, basket in enumerate(baskets):
            buckets[i//bucket_sz] = max(buckets[i//bucket_sz], basket)
        
        count = 0
        for fruit in fruits:
            unset = 1
            for i in range(buckets):
                if buckets[i] < fruit:
                    continue
                choosen = 0
                buckets[i] = 0
                for i in range(bucket_sz):
                    basket_pos = i * bucket_sz + i
                    if basket_pos < n and baskets[basket_pos] >= fruit and not choosen:
                        baskets[basket_pos] = 0
                        choosen = 1
                    if basket_pos < n:
                        buckets[i] = max(buckets[i], baskets[basket_pos])
                unset = 0
                break
            count += unset
        return count

fruits = [4,2,5]
baskets = [3,5,4]
ans = Solution().numOfUnplacedFruits(fruits, baskets)
print(ans)

fruits = [3,6,1]
baskets = [6,4,7]
ans = Solution().numOfUnplacedFruits(fruits, baskets)
print(ans)

fruits = [2,16,53,100,61]
baskets = [46,7,78,30,30]
ans = Solution().numOfUnplacedFruits(fruits, baskets)
print(ans)



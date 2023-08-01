from collections import deque
from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        n = len(warehouse)
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]
        left[0], right[n-1] = warehouse[0], warehouse[n-1]
        for i in range(1, n):
            left[i] = min(left[i-1], warehouse[i])
            right[n-1-i] = min(right[n-i], warehouse[n-i-1])
        space_use = [max(left[i], right[i]) for i in range(n)]
        space_use.sort()
        boxes.sort()

        ind = assign = 0
        for box in boxes:
            while ind < n and space_use[ind] < box:
                ind += 1
            if ind < n and space_use[ind] >= box:
                assign += 1
                ind += 1
        # print(space_use, assign)
        return assign

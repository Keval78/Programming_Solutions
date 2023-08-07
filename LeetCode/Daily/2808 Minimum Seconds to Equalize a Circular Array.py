'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        arr = nums + nums
        map_idx = {}
        for idx, num in enumerate(arr):
            if num in map_idx:
                curr_time = (idx-map_idx[num][0])//2
                # print(curr_time, idx, map_idx[num][0])
                map_idx[num] = [idx, max(curr_time, map_idx[num][1])]
            else:
                # print((idx+1)//2)
                map_idx[num] = [idx, (idx+1)//2]

        mini = float('inf')
        for val in map_idx.values():
            mini = min(mini, val[1])
        return mini

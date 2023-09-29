'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from sortedcontainers import SortedList


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        st = SortedList([0])
        res = pref = 0
        for i in range(n):
            pref += nums[i]
            l = st.bisect_right(pref-lower)
            r = st.bisect_left(pref-upper)
            res += l-r
            st.add(pref)
        return res

'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        cnt_zero = [0, 0]
        arr_sum = [0, 0]

        for num in nums1:
            arr_sum[0] += max(1, num)
            if num == 0:
                cnt_zero[0] += 1

        for num in nums2:
            arr_sum[1] += max(1, num)
            if num == 0:
                cnt_zero[1] += 1

        if arr_sum[0] == arr_sum[1]:
            return arr_sum[0]
        if arr_sum[0] > arr_sum[1] and cnt_zero[1] > 0:
            return arr_sum[0]
        elif arr_sum[0] < arr_sum[1] and cnt_zero[0] > 0:
            return arr_sum[1]
        return -1


nums1 = [3, 2, 0, 1, 0]
nums2 = [6, 5, 0]
ans = Solution().minSum(nums1, nums2)
print(ans)

nums1 = [2, 0, 2, 0]
nums2 = [1, 4]
ans = Solution().minSum(nums1, nums2)
print(ans)

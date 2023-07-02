"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from collections import defaultdict

def main():
    class Solution:
        def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
            last_ones, next_ones = -1, 0
            max_ones = 0
            for num in nums:
                if num==0:
                    last_ones = next_ones
                    next_ones = 0
                else:
                    next_ones += 1
                max_ones = max(max_ones, last_ones + next_ones + 1)
            return max_ones
        
        
            # longest_sequence = 0
            # left, right = 0, 0
            # num_zeroes = 0
            # while right < len(nums):
            #     if nums[right] == 0: num_zeroes += 1
            #     while num_zeroes == 2:
            #         if nums[left] == 0: num_zeroes -= 1
            #         left += 1
            #     longest_sequence = max(longest_sequence, right - left + 1)
            #     right += 1
            # return longest_sequence


    Solution().findMaxConsecutiveOnes()


if __name__ == "__main__":
    main()

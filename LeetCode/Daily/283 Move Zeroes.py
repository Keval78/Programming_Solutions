'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from collections import Counter

def main():
    class Solution:
        def moveZeroes(self, nums: List[int]) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
            count, j = 0, 0
            for i in nums:
                if i == 0:
                    count += 1
                else:
                    nums[j] = i
                    j+=1
            for i in range(1, count+1):
                nums[-i] = 0
            return nums
    
    Solution().moveZeroes()


if __name__ == "__main__":
    main()

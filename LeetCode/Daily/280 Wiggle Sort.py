"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

def main():
    class Solution:
        def wiggleSort(self, nums: List[int]) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
            for i in range(1,len(nums)):
                if ((i%2==1 and nums[i] < nums[i - 1]) or  (i%2==0 and nums[i] > nums[i - 1])):
                    nums[i - 1],nums[i] = nums[i],nums[i - 1]
            
    Solution().wiggleSort()


if __name__ == "__main__":
    main()

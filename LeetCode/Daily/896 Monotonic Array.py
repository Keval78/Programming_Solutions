'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def isMonotonic(self, nums: List[int]) -> bool:
            return all(nums[i]<=nums[i-1] for i in range(1, len(nums))) or all(nums[i]>=nums[i-1] for i in range(1, len(nums)))
    
    Solution().isMonotonic()


if __name__ == "__main__":
    main()

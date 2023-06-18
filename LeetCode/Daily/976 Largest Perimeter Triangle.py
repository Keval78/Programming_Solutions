'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def largestPerimeter(self, nums: List[int]) -> int:
            nums.sort()
            return max( sum(nums[i:i+3]) if nums[i]+nums[i+1]>nums[i+2] else 0 for i in range(len(nums)-2) )
            
    Solution().largestPerimeter()


if __name__ == "__main__":
    main()




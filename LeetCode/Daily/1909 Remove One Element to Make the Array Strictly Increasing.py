'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def canBeIncreasing(self, nums: list[int]) -> bool:
            def strictly_increasing(nums):
                for i in range(len(nums)-1):
                    if nums[i] >= nums[i+1]:
                        return False
                return True
            
            for i in range(len(nums)):
                if strictly_increasing(nums[:i]+nums[i+1:]):
                    return True
            return False
    
    Solution().canBeIncreasing([2,3,1,2])


if __name__ == "__main__":
    main()

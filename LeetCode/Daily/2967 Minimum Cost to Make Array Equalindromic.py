'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums)//2]
        s = str(median)
        n = len(s)

        m = (n//2+1) if n%2 else n//2
        pal = s[:m]
        
        pal1 = pal + pal[:n-m][::-1]
        if median < int(pal1):
            temp = str(int(pal) - 1)
            pal2 = (temp + temp[:n-m][::-1]) if temp != "0" else "9"
        else:
            temp = str(int(pal) + 1)
            pal2 = temp + temp[:n-m][::-1]

        ans1, ans2 = 0, 0
        for num in nums:
            ans1 += abs(num - int(pal1))
            ans2 += abs(num - int(pal2))

        return min(ans1, ans2)



nums = [1,2,3,4,5]
ans = Solution().minimumCost(nums)
print(ans)


nums = [10,12,13,14,15]
ans = Solution().minimumCost(nums)
print(ans)

nums = [22,33,22,33,22]
ans = Solution().minimumCost(nums)
print(ans)

nums = [5,2,1]
ans = Solution().minimumCost(nums)
print(ans)

nums = [301,309,312,322]
ans = Solution().minimumCost(nums)
print(ans)

nums = [150,722,102,628,272,539,753,161,814,930]
ans = Solution().minimumCost(nums)
print(ans)

nums = [9,10,10]
ans = Solution().minimumCost(nums)
print(ans)
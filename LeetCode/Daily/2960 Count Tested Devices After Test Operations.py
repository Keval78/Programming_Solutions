'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        decrease = 0
        for percentage in batteryPercentages:
            if percentage > decrease:
                decrease += 1
        return decrease


batteryPercentages = [1,1,2,1,3]
ans = Solution().countTestedDevices(batteryPercentages)
print(ans)

batteryPercentages = [0,1,2]
ans = Solution().countTestedDevices(batteryPercentages)
print(ans)


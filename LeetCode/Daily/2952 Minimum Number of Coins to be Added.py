'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        n = len(coins)
        prefSum = idx = added = 0
        for i in range(1, target+1):
            if i > prefSum:
                if idx<n and coins[idx] <= i:
                    prefSum += coins[idx]
                    idx += 1
                else:
                    prefSum += i
                    added += 1
        return added



coins = [1,4,10]
target = 19
ans = Solution().minimumAddedCoins(coins, target)
print(ans)


coins = [1,4,10,5,7,19]
target = 19
ans = Solution().minimumAddedCoins(coins, target)
print(ans)

coins = [1,1,1]
target = 20
ans = Solution().minimumAddedCoins(coins, target)
print(ans)



'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        import math

        def my_round(i):
            return math.floor(i) if i - math.floor(i) < 0.5 else math.floor(i)+1
        return 100 - my_round(purchaseAmount/10)*10

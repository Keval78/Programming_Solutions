'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''


class Solution:
    def countDigitOne(self, n: int) -> int:
        def digitdp(memo, num: str, idx: int, cnt: int, tight: int):
            if idx == len(num):
                return cnt

            if memo[idx][cnt][tight] != -1:
                return memo[idx][cnt][tight]

            res = 0
            low, high = 0, int(num[idx]) if tight else 9
            for i in range(low, high+1):
                res += digitdp(memo, num, idx+1, cnt+1 if i ==
                               1 else cnt, 1 if tight and i == int(num[idx]) else 0)

            memo[idx][cnt][tight] = res
            return res

        memo = [[[-1]*2 for i in range(10)] for j in range(10)]
        res = digitdp(memo, str(n), 0, 0, 1)
        return res

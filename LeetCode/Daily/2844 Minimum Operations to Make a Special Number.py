"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""


class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        s = ["52", "57", "00", "05"]

        def is_subsequence(x, y):
            ind = 0
            for i in range(len(y)):
                if x[ind] == y[i]:
                    ind += 1
                    if ind == len(x):
                        return i
            return -1

        revnum = num[::-1]
        res = float('inf')
        for sub in s:
            ans = is_subsequence(sub, revnum)
            if ans > 0:
                res = min(ans-1, res)

        cnt = 0
        for i in num:
            if i == '0':
                continue
            cnt += 1
        return min(res, cnt)

'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # 0 -> 0
        # 8 -> 8
        # 6 -> 9
        # 9 -> 6
        # 1 -> 1 (not sure)
        stbg = {'0': '0', '8': '8', '6': '9', '9': '6', '1': '1'}

        i, n = 0, len(num)
        while i <= n//2:
            if num[n-i-1] in stbg and num[i] == stbg[num[n-i-1]]:
                i += 1
                continue
            return False
        return True

'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''


class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(0, n, 2):
            if s[i] != s[i+1]:
                ans += 1
        return ans


s = "1001"
ans = Solution().minChanges(s)
print(ans)

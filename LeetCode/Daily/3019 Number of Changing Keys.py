'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

class Solution:
    def countKeyChanges(self, s: str) -> int:
        prev = s[0].lower()
        cnt = 0
        for ch in s:
            if ch.lower() != prev:
                prev = ch.lower()
                cnt += 1
        return cnt


s = "aAbBcC"
ans = Solution().countKeyChanges(s)
print(ans)

s = "AaAaAaaA"
ans = Solution().countKeyChanges(s)
print(ans)

'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''


class Solution:
    def finalString(self, s: str) -> str:
        ans = []
        for char in s:
            if char == "i":
                ans = ans[::-1]
            else:
                ans.append(char)
        return ''.join(ans)

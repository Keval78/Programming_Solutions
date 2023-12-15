'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        seq = 1
        ans = 0
        for i in range(1, len(word)):
            if abs(ord(word[i])-ord(word[i-1])) < 2:
                seq += 1
            else:
                ans += seq//2
                seq = 1
        ans += seq//2
        return ans


word = "aaaaa"
ans = Solution().removeAlmostEqualCharacters(word)
print(ans)

word = "abddez"
ans = Solution().removeAlmostEqualCharacters(word)
print(ans)

word = "zyxyxyz"
ans = Solution().removeAlmostEqualCharacters(word)
print(ans)

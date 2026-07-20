'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from collections import Counter

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter = Counter(s)
        ans, set_ans = [], set()
        for ch in s:
            if ch not in set_ans:
                while ans and ans[-1] > ch and counter[ans[-1]] > 0:
                    set_ans.remove(ans[-1])
                    ans.pop()
                set_ans.add(ch)
                ans.append(ch)
            counter[ch] -= 1
        return "".join(ans)

s = "bcabc"
ans = Solution().smallestSubsequence(s)
print(ans)

s = "cbacdcbc"
ans = Solution().smallestSubsequence(s)
print(ans)


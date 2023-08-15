from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = ["", "", "abc", "def", "ghi",
                   "jkl", "mno", "pqrs", "tuv", "wxyz"]

        ans = [""]
        choosen = []
        for digit in digits:
            ind = int(digit)
            n = len(ans)
            for i in range(n):
                s = ans[i]
                for ch in letters[ind]:
                    ans.append(s+ch)
            ans = ans[n:]

        return [] if len(ans) == 1 else ans

"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from collections import defaultdict

def main():
    class Solution:
        def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
            i, j, n = 0, 0, len(s)
            distinct = defaultdict()
            max_substr = 0
            while (j<n):
                distinct[s[j]] = j
                j+=1
                if len(distinct) == k+1:
                    del_idx = min(distinct.values())
                    del distinct[s[del_idx]]
                    i = del_idx+1
                max_substr = max(max_substr, j-i)
            return max_substr
            
    Solution().lengthOfLongestSubstringKDistinct()


if __name__ == "__main__":
    main()

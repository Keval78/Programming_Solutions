class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        # Approach: Sliding Window
        L, R = 0, 0
        visit = {}
        max_len = 0
        while R < n:
            if s[R] in visit:
                L = max(L, visit[s[R]] + 1)
            visit[s[R]] = R
            ans = R-L+1
            R += 1
            max_len = max(max_len, ans)
        return max_len

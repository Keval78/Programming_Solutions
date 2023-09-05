'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # TLE
        # n = len(s)
        # char_map = [[] for i in range(n)]
        # for word in wordDict:
        #     res = [i for i in range(len(s)) if s.startswith(word, i)]
        #     for ind in res:
        #         char_map[ind].append((ind, ind+len(word)))

        # def dfs(char_map, i):
        #     if i==len(char_map):
        #         return True
        #     if len(char_map[i]) == 0:
        #         return False
        #     for j in range(len(char_map[i])):
        #         if dfs(char_map, char_map[i][j][1]):
        #             return True
        #     return False

        # return dfs(char_map, 0)

        # DP: O(n⋅m⋅k)
        # n = len(s)
        # dp = [False]*n
        # for i in range(len(s)):
        #     for word in wordDict:
        #         m = len(word)
        #         if i < m-1: continue
        #         if (i==m-1 or dp[i-m]) and s[i-m+1:i+1]==word:
        #             dp[i] = True
        #             break
        # return dp[-1]

        # DP + Trie: O(n⋅k + m⋅k)
        def find(root, s, i, dp):
            if root.is_word:
                dp[i] = True
            if i+1 >= len(s) or s[i+1] not in root.children:
                return
            find(root.children[s[i+1]], s, i+1, dp)

        root = TrieNode()
        for word in wordDict:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.is_word = True

        n = len(s)
        dp = [False]*n
        s = list(s)
        for i in range(n):
            if i == 0 or dp[i - 1]:
                # Find word from s[i] to... in Trie and set all end True
                find(root, s, i-1, dp)
        return dp[-1]

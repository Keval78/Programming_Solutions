'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from dataclasses import dataclass, field
from typing import List, Optional
from collections import defaultdict

@dataclass
class TrieNode:
    """Dataclass represing node of the trie.
    """
    end_cnt: int = 0
    children: 'TrieNode' = field(default_factory=lambda: defaultdict(TrieNode))


class Trie:
    """Trie/PrefixTree data structure.
    """
    def __init__(self) -> None:
        self.root: Optional['TrieNode'] = TrieNode()
        self.ans = 0

    def insert(self, word: str) -> None:
        """Inserts a word into the Trie
        """
        curr = self.root
        for i in range(len(word)):
            key = word[i] + word[len(word)-i-1]
            if key not in curr.children:
                curr.children[key] = TrieNode()
            curr = curr.children[key]
            self.ans += curr.end_cnt
        curr.end_cnt += 1


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """Solve it using Trie.
        """
        n = len(words)
        trie = Trie()
        
        for word in words:
            # For each word calculate Prefix = Suffix indices.
            trie.insert(word)

        return trie.ans


words = ["a","aba","ababa","aa"]
ans = Solution().countPrefixSuffixPairs(words)
print(ans)

words = ["pa","papa","ma","mama"]
ans = Solution().countPrefixSuffixPairs(words)
print(ans)

words = ["abab","ab"]
ans = Solution().countPrefixSuffixPairs(words)
print(ans)

words = ["ab","abc"]
ans = Solution().countPrefixSuffixPairs(words)
print(ans)
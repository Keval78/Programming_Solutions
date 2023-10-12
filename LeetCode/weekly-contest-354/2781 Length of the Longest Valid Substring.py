from typing import List


class Trie:
    def __init__(self):
        self.is_leaf: bool = False
        self.nodes = {}

    def insert(self, word):
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = Trie()
            curr = curr.nodes[char]
        curr.is_leaf = True

    def print_words(self, word: str = ""):
        if self.is_leaf:
            print(word, end=" ")
        for key, value in self.nodes.items():
            value.print_words(word + key)

    def find_substr(self, word: str):
        curr = self
        # print("Searching..", word)
        for i, char in enumerate(word):
            if char not in curr.nodes:
                return False
            if curr.nodes[char].is_leaf:
                return True
            curr = curr.nodes[char]
        return curr.is_leaf

    def __str__(self):
        self.print_words()
        return ''


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        root = Trie()
        for s in forbidden:
            root.insert(s)

        end = len(word)-1
        curr = ''
        maxi = 0
        for i in range(len(word)-1, -1, -1):
            curr = word[i] + curr
            # ans = root.find_substr(curr)
            while root.find_substr(curr):
                end -= 1
                curr = curr[:-1]
            maxi = max(maxi, end-i+1)
        return maxi

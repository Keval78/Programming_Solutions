from typing import List
import collections


class Solution:
    def sortVowels(self, s: str) -> str:
        indices = collections.deque()
        vowels = [0 for i in range(10)]
        s = list(s)
        pos = {
            'A': 0,
            'E': 1,
            'I': 2,
            'O': 3,
            'U': 4,
            'a': 5,
            'e': 6,
            'i': 7,
            'o': 8,
            'u': 9
        }

        for i, char in enumerate(s):
            if char in pos:
                vowels[pos[char]] += 1
                indices.append(i)

        iv = 0
        for ind in indices:
            while vowels[iv] == 0:
                iv += 1
            for k, v in pos.items():
                if iv == v:
                    s[ind] = k
                    vowels[iv] -= 1
                    break
        return "".join(s)

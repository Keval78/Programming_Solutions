"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

import collections
from typing import List, Optional


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for a, b in adjacentPairs:
            adj[a].append(b)
            adj[b].append(a)

        nums = []
        seen = set()

        def dfs(num):
            seen.add(num)
            for nnum in adj[num]:
                if nnum not in seen:
                    dfs(nnum)
            nums.append(num)

        start = -1
        for k, v in adj.items():
            if len(v) == 1:
                start = k
                break

        dfs(start)
        return nums

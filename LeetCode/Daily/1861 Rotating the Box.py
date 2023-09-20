"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n, m = len(box), len(box[0])
        for i in range(n):
            queue = []
            for j in range(m-1, -1, -1):
                # print(i,j, queue)
                if box[i][j] == ".":
                    queue.append(j)
                if box[i][j] == "*":
                    queue.clear()
                if box[i][j] == "#":
                    if queue:
                        box[i][queue.pop(0)] = "#"
                        box[i][j] = "."
                        queue.append(j)
        # print(box)
        rbox = []
        for j in range(m):
            rbox.append([])
            for i in range(n-1, -1, -1):
                rbox[-1].append(box[i][j])
        return rbox

"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List, Optional


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visit = [[False]*n for i in range(n)]

        def getindices(npos):
            row = n - (npos-1)//n - 1
            if row % 2 == n % 2:  # increasing
                col = n - (npos-1) % n - 1
            else:  # decreasing
                col = (npos-1) % n
            return row, col

        que = [(1, 0)]
        visit[n-1][0] = True

        while que:
            pos, steps = que.pop(0)
            if pos == n*n:
                return steps

            for i in range(6):
                npos = pos + i + 1
                if npos > (n*n):
                    continue

                r, c = getindices(npos)
                # Check for snake or ladder
                if board[r][c] != -1:
                    npos = board[r][c]
                    r, c = getindices(npos)

                # Node already in the que or processed inside que.
                if visit[r][c]:
                    continue
                visit[r][c] = True
                que.append((npos, steps+1))
                # print(npos, que)
        return -1

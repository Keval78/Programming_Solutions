"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        def findandzero(board):
            n, m = len(board), len(board[0])
            candies = set()
            # Horizontal candies >= 3.
            for i in range(n):
                for j in range(m-2):
                    if board[i][j] != 0 and board[i][j] == board[i][j+1] == board[i][j+2]:
                        candies.add((i, j))
                        candies.add((i, j+1))
                        candies.add((i, j+2))

            for i in range(n-2):
                for j in range(m):
                    if board[i][j] != 0 and board[i][j] == board[i+1][j] == board[i+2][j]:
                        candies.add((i, j))
                        candies.add((i+1, j))
                        candies.add((i+2, j))

            for i, j in candies:
                board[i][j] = 0
            return len(candies)

        def dropcandy(board):
            n, m = len(board), len(board[0])
            for j in range(m):
                # drop using queue
                idx = n-1
                for i in range(n-1, -1, -1):
                    if board[i][j] != 0:
                        board[idx][j] = board[i][j]
                        idx -= 1

                while idx >= 0:
                    board[idx][j] = 0
                    idx -= 1

        while findandzero(board) != 0:
            dropcandy(board)

        return board

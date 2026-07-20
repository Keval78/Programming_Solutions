'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row_len, col_len = len(grid), len(grid[0])
        k %= (row_len*col_len)
        if k == 0:
            return grid
        transferred = set()
        for s in range(row_len*col_len):
            start = s
            temp = grid[start // col_len][start % col_len]
            while start not in transferred:
                next_ = (start + k) % (row_len*col_len)
                nrow, ncol = next_ // col_len, next_ % col_len
                temp, grid[nrow][ncol] = grid[nrow][ncol], temp
                transferred.add(start)
                start = next_
        return grid


grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
ans = Solution().shiftGrid(grid, k)
print(ans)


grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
ans = Solution().shiftGrid(grid, k)
print(ans)


grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 9
ans = Solution().shiftGrid(grid, k)
print(ans)



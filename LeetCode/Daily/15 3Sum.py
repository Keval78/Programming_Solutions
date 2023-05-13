"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List

def main():
    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            if(i<0 or j<0 or i>len(grid)-1 or j>len(grid[i])-1): return
            if grid[i][j]=="1":
                grid[i][j]="0"
                self.traversal(i-1, j, grid)
                self.traversal(i+1, j, grid)
                self.traversal(i, j-1, grid)
                self.traversal(i, j+1, grid)

        def numIslands(self, grid: List[List[str]]) -> int:
            tot = 0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == "1":
                        tot += 1
                        self.traversal(i, j, grid)
                        
            return tot
            
    Solution().threeSum()


if __name__ == "__main__":
    main()

'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def findMissingAndRepeatedValues2(self, grid: List[List[int]]) -> List[int]:
        # TODO: Solution Approach 1
        # TODO: Using XOR
        
        # * Find xor of all values. and xor of [1..N]
        # * xor = a^b.
        # * Find the rightmost set bit => x & -x
        
        a = b = xor = 0
        idx, n = 1, len(grid)
        
        for i in range(n):
            for j in range(n):
                xor ^= grid[i][j] ^ idx
                idx += 1 
        
        print(xor)
        set_bit_no = xor & -xor
        print(set_bit_no)

        idx = 1
        for i in range(n):
            for j in range(n):
                a ^= grid[i][j] if grid[i][j] & set_bit_no else 0
                a ^= idx if idx & set_bit_no else 0
                idx += 1
        
        b = a^xor
        print(a, b)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == a:
                    return [a, b]
        return [b, a]
    

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """Solution Approach 2
        """
        # TODO: Solution Approach 2
        # TODO: Using Negative indexing
        n = len(grid)
        ans = [-1, -1]
        
        for i in range(n):
            for j in range(n):
                idx = abs(grid[i][j])
                ni, nj = idx//n, idx%n
                if ni == n: ni, nj = 0, 0

                if grid[ni][nj] < 0:
                    ans[0] = idx
                else:
                    grid[ni][nj] = -grid[ni][nj]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    idx = i*n + j
                    if idx == 0: idx = n*n
                    ans[1] = idx

        return ans



grid = [[1,3],[2,2]]
ans = Solution().findMissingAndRepeatedValues(grid)
print(ans)

grid = [[9,1,7],[8,9,2],[3,4,6]]
ans = Solution().findMissingAndRepeatedValues(grid)
print(ans)


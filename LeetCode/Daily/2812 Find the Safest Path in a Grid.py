'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from collections import deque


class Solution:
    def maximumSafenessFactor(self, grid) -> int:
        # grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
        n, m = len(grid), len(grid[0])
        que = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    grid[i][j] = -1
                else:
                    grid[i][j] = 0
                    que.append((i, j))

        moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        while len(que) > 0:
            i, j = que.popleft()
            for dx, dy in moves:
                new_i = i + dx
                new_j = j + dy
                if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == -1:
                    grid[new_i][new_j] = grid[i][j] + 1
                    que.append((new_i, new_j))

        max_safness = min(grid[0][0], grid[n-1][m-1])
        # print(max_safness)

        # for gri in grid:
        #     print(gri)

        parents = [-1 for i in range(n*m)]

        for safness in range(max_safness, -1, -1):
            is_possible = False
            visit = [[False for i in range(m)] for j in range(n)]
            que = deque([(0, 0)])
            visit[0][0] = True
            while len(que) > 0:
                i, j = que.popleft()
                if i == n-1 and j == m-1:
                    # return safness
                    is_possible = True
                    break
                for dx, dy in moves:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and not visit[ni][nj] and grid[ni][nj] >= safness:
                        parents[ni*n + nj] = i*n + j
                        visit[ni][nj] = True
                        que.append((ni, nj))
            if is_possible:
                print(safness)
                break

        # for i in range(n):
        #     print(parents[i*n:(i+1)*n])

        curr = parents[-1]
        while curr != -1:
            print(f"({curr//n}, {curr%n})", end="->")
            curr = parents[curr]
        print()


# grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
# grid = [[0,1,1],[0,1,1],[1,1,0]]
grid = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

Solution().maximumSafenessFactor(grid)

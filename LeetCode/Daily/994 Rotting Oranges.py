class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        que = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    que.append([i,j])

        # visit = [[False]*m for i in range(n)]
        moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        while que:
            i, j = que.popleft()
            for di, dj in moves:
                if 0<=i+di<n and 0<=j+dj<m and grid[i+di][j+dj]==1:
                    grid[i+di][j+dj] = grid[i][j] + 1
                    que.append([i+di, j+dj])
        if any([1 in x for x in grid]): return -1
        time = max([max(x) for x in grid])
        if time == 0: return 0
        return time-2
            


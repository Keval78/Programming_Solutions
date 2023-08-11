class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        heap = [(0, 0, (0, 0))]
        visited = [[False]*m for i in range(n)] 
        moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        while heap:
            effort, min_effort, (i, j) = heappop(heap)
            if visited[i][j]: continue
            visited[i][j] = True
            if i==n-1 and j==m-1: return min_effort

            for dx, dy in moves:
                di, dj = i + dx, j + dy
                if 0<=di<n and 0<=dj<m and not visited[di][dj]:
                    path_effort = abs(heights[di][dj] - heights[i][j])
                    heappush(heap, (path_effort, max(min_effort, path_effort), (di, dj)))
        return 0
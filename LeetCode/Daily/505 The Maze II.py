class Solution:
    def shortestDistance(self, maze, start, destination):
        i, j = start
        m, n = len(maze), len(maze[0])
        
        visit = [False]*(m*n)
        que = [(0, i, j)]
        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        while que:
            steps, i, j = heappop(que)
            visit[n*i + j] = True
            if [i, j] == destination: return steps
            for di, dj in moves:
                ni, nj, cnt = i+di, j+dj, 0
                while 0<=ni<m and 0<=nj<n and maze[ni][nj]!=1:
                    ni, nj, cnt = ni+di, nj+dj, cnt+1
                ni, nj = ni-di, nj-dj,
                if not visit[n*ni+nj]:
                    heappush(que, (steps+cnt, ni, nj))
        return -1
class Solution:
    def hasPath(self, maze, start, destination):
        i, j = start
        m, n = len(maze), len(maze[0])
        
        visit = [False]*(m*n)
        que = deque([(i,j)])
        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        while que:
            i, j = que.popleft()
            visit[n*i + j] = True
            if [i, j] == destination: return True
            for di, dj in moves:
                ni, nj = i+di, j+dj
                while 0<=ni<m and 0<=nj<n and maze[ni][nj]!=1:
                    ni, nj = ni+di, nj+dj
                ni, nj = ni-di, nj-dj
                if not visit[n*ni+nj]:
                    que.append((ni, nj))
        return False
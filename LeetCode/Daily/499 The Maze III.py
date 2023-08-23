class Solution:
    def findShortestWay(self, maze, ball, hole):
        i, j = ball
        m, n = len(maze), len(maze[0])
        
        visit = [False]*(m*n)
        que = [(0, "", i, j)]
        moves = [(-1, 0, 'u'), (0, -1, 'l'), (1, 0, 'd'), (0, 1, 'r')]
        min_steps = float('inf')
        ans = "impossible"
        while que:
            steps, path, i, j = heappop(que)
            visit[n*i + j] = True
            for di, dj, dire in moves:
                ni, nj, cnt = i+di, j+dj, 0
                while 0<=ni<m and 0<=nj<n and maze[ni][nj]!=1:
                    if [ni, nj] == hole: 
                        if steps+cnt+1 <= min_steps:
                            if steps+cnt+1 < min_steps:
                                min_steps = steps+cnt+1
                                ans = path + dire
                            else:
                                if ans > path + direction[(di, dj)]:
                                    ans = path + dire

                    ni, nj, cnt = ni+di, nj+dj, cnt+1

                ni, nj = ni-di, nj-dj,
                if not visit[n*ni+nj] and steps+cnt < min_steps:
                    heappush(que, (steps+cnt, path + dire, ni, nj))
        return ans
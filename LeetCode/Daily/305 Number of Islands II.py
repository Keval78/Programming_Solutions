class DisjointSet:
    def __init__(self, n):
        self.rank = [0 for i in range(n)]
        self.parent = [-1 for i in range(n)]
        self.nsets = 0
    
    def make_set(self, x):
        if self.parent[x] != -1: return
        self.parent[x] = x
        self.nsets += 1

    def find_set(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]
    
    def union_set(self, x, y):
        x, y = self.find_set(x), self.find_set(y)
        if x == y:
            return

        if self.rank[x] == self.rank[y]:
            self.parent[x] = y
            self.rank[y] += 1
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
        self.nsets -= 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # m -> rows, n -> columns, position is m*i + n
        djset = DisjointSet(m*n)

        islands = []
        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i, j in positions:
            pos = n*i + j
            djset.make_set(pos)

            for di, dj in moves:
                ni, nj = i+di, j+dj
                npos = ni*n+nj
                if 0<=ni<m and 0<=nj<n and djset.parent[npos] != -1:
                    djset.union_set(pos, npos)
            
            islands.append(djset.nsets)
            # print(djset.nsets)
            
        
        return islands

            






class Solution:
    def find_island(self, i, j, visited, grid, islands):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return
        if not visited[i][j] and grid[i][j] == 1:
            islands[-1].append((i, j))
            visited[i][j] = True
            self.find_island(i-1, j, visited, grid, islands)
            self.find_island(i, j-1, visited, grid, islands)
            self.find_island(i+1, j, visited, grid, islands)
            self.find_island(i, j+1, visited, grid, islands)

    def match(self, identic, island):
        if len(identic) != len(island):
            return False
        i, j = identic[0][0]-island[0][0], identic[0][1] - island[0][1]
        for first, second in zip(sorted(identic), sorted(island)):
            if i != first[0]-second[0] or j!=first[1]-second[1]:
                return False
        return True

    def numDistinctIslands1(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        visited = [[False for i in range(m)] for j in range(n)]
        islands = []

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == 1:
                    islands.append([])
                    self.find_island(i, j, visited, grid, islands)
        
        
        identics = []
        for island in islands:
            if not identics:
                identics.append(island)
            else:
                for identic in identics:
                    if self.match(identic, island):
                        break
                else:
                    identics.append(island)
        #print(identics)
        return len(identics)

    # Hashing Solution: O((N⋅M)
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        def dfs(i, j, direction):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]): return
            if not visited[i][j] and grid[i][j]==1:
                visited[i][j] = True
                path_signature.append(direction)
                dfs(i + 1, j, "D")
                dfs(i - 1, j, "U")
                dfs(i, j + 1, "R")
                dfs(i, j - 1, "L")
                path_signature.append("0")
        
        
        n, m = len(grid), len(grid[0])
        visited = [[False for i in range(m)] for j in range(n)]
        uniq_islands = set()
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == 1:
                    path_signature = []
                    dfs(i, j, "0")
                    uniq_islands.add("".join(path_signature))
        
        #print(uniq_islands)
        return len(uniq_islands)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int, curr = -1) -> List[List[int]]:
        if curr == -1: curr = image[sr][sc]
        n, m = len(image), len(image[0])
        moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        if image[sr][sc] != color and image[sr][sc] == curr:
            image[sr][sc] = color
            for dx, dy in moves:
                if 0 <= sr + dx < n and 0 <= sc + dy < m and image[sr+dx][sc+dy] != color and image[sr+dx][sc+dy] == curr:
                    self.floodFill(image, sr + dx, sc + dy, color, curr)        
        return image

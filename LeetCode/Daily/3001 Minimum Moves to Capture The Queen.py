'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''


class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        def check_in_path(start, direction, obj):
            for i in range(8):
                start[0], start[1] = start[0]+direction[0], start[1]+direction[1]
                if start == obj: return True
                if start == [e, f]: return False
            return False
        
        min_move = 2

        # For White rook
        if a == e:
            # print(check_in_path([a, b], (, 0), [c, d]))
            if not check_in_path([a, b], (0, -1 if b>f else 1), [c, d]):
                min_move = 1
        if b == f:
            if not check_in_path([a, b], (-1 if a>e else 1, 0), [c, d]):
                min_move = 1

        # print("min_move", min_move)
        # # For White bishop
        if abs(c-e) == abs(d-f):
            if not check_in_path([c, d], (-1 if c>e else 1, -1 if d>f else 1), [a, b]):
                min_move = 1

        return min_move
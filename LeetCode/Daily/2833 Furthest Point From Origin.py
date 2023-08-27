"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return max(moves.count('L'), moves.count('R')) + moves.count('_') - min(moves.count('L'), moves.count('R'))

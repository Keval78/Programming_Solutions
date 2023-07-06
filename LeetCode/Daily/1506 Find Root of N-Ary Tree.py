"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        value_sum = 0
        for node in tree:
            value_sum += node.val
            for child in node.children:
                value_sum -= child.val
        
        for node in tree:
            if node.val == value_sum:
                return node
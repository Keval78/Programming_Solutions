"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

class Solution:
    def dfs(self, root):
        if root is None: return [0, 0] 
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        curr_sum, nodes = root.val+left[0]+right[0], 1+left[1]+right[1]
        self.max_avg = max(self.max_avg, curr_sum/nodes)
        return [curr_sum, nodes]

    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.max_avg = 0
        self.dfs(root)
        return self.max_avg

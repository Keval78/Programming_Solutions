"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

class Solution:
    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        left = self.dfs(root.left) + 1
        right = self.dfs(root.right) + 1
        if root.left is not None and root.left.val != root.val+1: left = 1
        if root.right is not None and root.right.val != root.val+1: right = 1
        self.maxlen = max(self.maxlen, left, right)
        return max(left, right)

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.maxlen: int = 0
        self.dfs(root)
        return self.maxlen

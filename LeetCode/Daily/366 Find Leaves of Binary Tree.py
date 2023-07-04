"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs_leaf(root):
            if root is None: return None
            if root.left is None and root.right is None:
                leaves[-1].append(root.val)
                return None
            root.left = dfs_leaf(root.left)
            root.right = dfs_leaf(root.right)
            return root
        
        leaves = []
        while root:
            leaves.append([])
            root = dfs_leaf(root)
        return leaves

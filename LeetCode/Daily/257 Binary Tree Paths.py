"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def inorder(root, stack, res):
            if root.left is None and root.right is None:
                res.append("->".join(stack + [str(root.val)]))
                return

            stack.append(str(root.val))
            if root.left:
                inorder(root.left, stack, res)
            if root.right:
                inorder(root.right, stack, res)
            stack.pop()

        res = []
        inorder(root, [], res)

        return res

'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            if left > right:
                return None
            root = TreeNode(postorder.pop())
            part_ind = idx_map[root.val]
            root.right = build(part_ind+1, right)
            root.left = build(left, part_ind-1)
            return root
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        n = len(inorder)
        return build(0, n-1)

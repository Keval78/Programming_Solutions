"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from dataclasses import dataclass
from typing import Any

@dataclass
class NodeValue:
    min_node: Any
    max_node: Any
    max_size: Any

class Solution:
    def islargestBSTSubtree(self, root: Optional[TreeNode]) -> NodeValue:
        if root is None: 
            return NodeValue(float('inf'), float('-inf'), 0)
        left = self.islargestBSTSubtree(root.left)
        right = self.islargestBSTSubtree(root.right)
        if left.max_node < root.val < right.min_node:
            return NodeValue(min(root.val, left.min_node), max(root.val, right.max_node), left.max_size + right.max_size + 1)
        return NodeValue(float('-inf'), float('inf'), max(left.max_size, right.max_size))

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        return self.islargestBSTSubtree(root).max_size
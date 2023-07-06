"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
class Solution:
    def find(self, root: TreeNode, data: int) -> TreeNode:
        """Find the node if it exist in the tree.
        """
        curr = root
        while curr is not None and curr.val != data:
            curr = curr.left if data < curr.val else curr.right
        return curr

    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        if root1 is None: return False
        node = self.find(root2, (target-root1.val))
        if node is not None: return True
        else: return self.twoSumBSTs(root1.left, root2, target) or self.twoSumBSTs(root1.right, root2, target)
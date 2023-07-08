"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.maxval=0
        def longest_path(root: TreeNode) -> List[int]:
            # for None [inc=0, dec=0]
            if not root: return [0, 0]
            
            inr = dcr = 1
            left = longest_path(root.left)
            right = longest_path(root.right)
            
            if root.left and (root.val == root.left.val + 1):
                dcr = left[1] + 1
            if root.right and (root.val == root.right.val + 1):
                dcr = max(dcr, right[1] + 1)
            
            if root.left and (root.val == root.left.val - 1):
                inr = left[0] + 1
            if root.right and (root.val == root.right.val - 1):
                inr = max(inr, right[0] + 1)
                    
            self.maxval = max(self.maxval, dcr + inr - 1)
            return [inr, dcr]
        
        longest_path(root)
        return self.maxval

"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

def main():
    class Solution:
        curr = 0
        def bstToGst(self, root: TreeNode) -> TreeNode:
            if root is None:
                return
            self.bstToGst(root.right)
            self.curr += root.val
            root.val = self.curr
            self.bstToGst(root.left)
            return root
            
    Solution().bstToGst()


if __name__ == "__main__":
    main()

'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def minDepth(self, root: Optional[TreeNode]) -> int:
            if root is None: return 0
            if root.left is None and root.right is None: return 1
            if root.left and root.right:
                return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
            return 1 + self.minDepth(root.left if root.left else root.right)

    Solution().minDepth()


if __name__ == "__main__":
    main()




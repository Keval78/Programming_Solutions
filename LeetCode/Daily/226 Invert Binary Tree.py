'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root:
                root.left, root.right = root.right, root.left
                self.invertTree(root.left)
                self.invertTree(root.right)
            return root

    Solution().invertTree()


if __name__ == "__main__":
    main()




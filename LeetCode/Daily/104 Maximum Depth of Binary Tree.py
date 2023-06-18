'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def maxDepth(self, root: Optional[TreeNode]) -> int:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0

    Solution().maxDepth()


if __name__ == "__main__":
    main()




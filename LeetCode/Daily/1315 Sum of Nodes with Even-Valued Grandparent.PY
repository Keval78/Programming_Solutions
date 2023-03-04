"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

def main():
    class Solution:
        def sumEvenGrandparent(self, root: TreeNode) -> int:
            def custom_dfs(root: TreeNode, grandparent: bool, parent: bool):
                if root is None: return 0
                if grandparent:
                    yield root.val
                grandparent = parent
                parent = True if root.val%2==0 else False
                yield from custom_dfs(root.left, grandparent, parent)
                yield from custom_dfs(root.right, grandparent, parent)
            tot = 0
            for val in custom_dfs(root, False, False):
                tot += val
            return tot
    Solution().sumEvenGrandparent()


if __name__ == "__main__":
    main()

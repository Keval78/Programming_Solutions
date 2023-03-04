"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import Optional
def main():
    class Solution:
        def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
            valid_nodes = 0
            def custom_postorder(root: Optional[TreeNode])->List[int]:
                nonlocal valid_nodes
                if root is None: return [0, 0]
                nodes, tot = 0, 0
                val1 = custom_postorder(root.left)
                val2 = custom_postorder(root.right)
                nodes += val1[0]+val2[0]+1
                tot += val1[1]+val2[1]+root.val
                if tot//nodes == root.val:
                    valid_nodes+=1
                return [nodes, tot]
            custom_postorder(root)
            return valid_nodes
            
    Solution().sumEvenGrandparent()


if __name__ == "__main__":
    main()

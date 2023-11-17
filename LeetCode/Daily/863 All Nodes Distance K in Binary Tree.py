'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        DFS with Prunning.
        Another way to solve the problem is to add parent pointer and do dfs.
        
        Args:
            root (TreeNode): _description_
            target (TreeNode): _description_
            k (int): _description_

        Returns:
            List[int]: _description_
        """
        data = []
        def subtree_search(root, k, prune = "None"):
            if k == 0:
                data.append(root.val)
            else:
                if prune != "left" and root.left:
                    subtree_search(root.left, k-1)
                if prune != "right" and root.right:
                    subtree_search(root.right, k-1)
        
        def dfs(root, target):
            if root is None: return -1
            if root.val == target.val:
                subtree_search(root, k)
                return 1
            else:
                ans = dfs(root.left, target)
                if ans > 0:
                    # print(root.val, k-ans, "left")
                    subtree_search(root, k-ans, "left")
                    return ans+1
                
                ans = dfs(root.right, target)
                if ans > 0:
                    # print(root.val, k-ans, "right")
                    subtree_search(root, k-ans, "right")
                    return ans+1
                
                return -1
        
        dfs(root, target)
        # print(data)
        return data

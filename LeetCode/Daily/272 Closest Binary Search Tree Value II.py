"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find(self, root: TreeNode, data: int) -> TreeNode:
        """Find the node if it exist in the tree.
        """
        curr = root
        while curr is not None and curr.val != data:
            curr = curr.left if data < curr.val else curr.right
        return curr

    def successor(self, root: TreeNode, data: int) -> TreeNode:
        """Find the Successor node of the given node,
        the node with the smallest key greater than the key of the input node.
        """
        node = self.find(root, data)
        if node is None:
            return

        # if node has child available then search in subtree
        node = node.right

        if node is None:
            # succ = self.find_parent(root, data)
            succ = None
            while (root):
                if (root.val < data):
                    root = root.right
                elif (root.val > data):
                    succ, root = root, root.left
                else:
                    break
            return succ

        while node.left:
            node = node.left
        return node

    def predecessor(self, root: TreeNode, data: int) -> TreeNode:
        """Find the Predecessor node of the given node,
        the maximum value in its left subtree.
        """
        node = self.find(root, data)
        if node is None:
            return

        # if node has child available then search in subtree
        node = node.left

        if node is None:
            pred = None
            while (root):
                if (root.val < data):
                    pred, root = root, root.right
                elif (root.val > data):
                    root = root.left
                else:
                    break
            return pred

        while node.right:
            node = node.right
        return node

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        k_close = []
        # First closest value
        curr, ans = root, root
        while curr:
            ans = min(curr, ans, key=lambda x: (abs(target - x.val), x.val))
            curr = curr.left if target < curr.val else curr.right
        k_close.append(ans)
        # print(k_close)
        curr_pred = self.predecessor(root, ans.val)
        curr_succ = self.successor(root, ans.val)
        while len(k_close) < k:
            # print(curr_pred, curr_succ)
            if curr_pred is None:
                while len(k_close) < k:
                    k_close.append(curr_succ)
                    curr_succ = self.successor(root, curr_succ.val)
            elif curr_succ is None:
                while len(k_close) < k:
                    k_close.append(curr_pred)
                    curr_pred = self.predecessor(root, curr_pred.val)
            else:
                if abs(target-curr_pred.val) <= abs(target-curr_succ.val):
                    k_close.append(curr_pred)
                    curr_pred = self.predecessor(root, curr_pred.val)
                else:
                    k_close.append(curr_succ)
                    curr_succ = self.successor(root, curr_succ.val)

        return [x.val for x in k_close]

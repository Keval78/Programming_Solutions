'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        root = p
        while root.parent is not None:
            root = root.parent

        def lca(root, p, q):
            if root is None or p == root or q == root:
                return root
            left = lca(root.left, p, q)
            right = lca(root.right, p, q)
            if left is None:
                return right
            elif right is None:
                return left
            else:
                return root
        return lca(root, p, q)

    # Time Complexity: O(H)
    # Space Complexity: O(1)
    # Instead of precalculating the length of each path, we can use the fact that a+b == b+a to get both nodes on the same level on the tree.
    # We can say there are two different paths: q_path and p_path
    # You u can essentially create two equally sized, but different paths.
    # a_path = q_path + p_path
    # b_path = p_path + q_path
    # def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
    #     a_node = p
    #     b_node = q

    #     while a_node != b_node:
    #         if a_node.parent:
    #             a_node = a_node.parent
    #         else:
    #             a_node = q

    #         if b_node.parent:
    #             b_node = b_node.parent
    #         else:
    #             b_node = p
    #     return a_node

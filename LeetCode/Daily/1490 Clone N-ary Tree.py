'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        new_node = Node(root.val)
        for child in root.children:
            new_node.children.append(self.cloneTree(child))
        return new_node

    # Time Complexity: O(M)O(M)O(M)
    # Space Complexity: O(log⁡nM)
    # def cloneTree(self, root: 'Node') -> 'Node':
    #     if not root: return root

    #     new_root = Node(root.val)
    #     # Starting point to kick off the DFS visits.
    #     stack = [(root, new_root)]

    #     while stack:
    #         old_node, new_node = stack.pop()
    #         for child_node in old_node.children:
    #             new_child_node = Node(child_node.val)

    #             # Make a copy for each child node.
    #             new_node.children.append(new_child_node)

    #             # Schedule a visit to copy the child nodes of each child node.
    #             stack.append((child_node, new_child_node))

    #     return new_root

"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
class Solution:
    def boundry_traversal(self, root):
        """Boundery Traversal
            1. Left Boundry excluding leaf.
            2. Leaf Nodes.
            3. Right Boundry excluding leaf.
        """
        result = []
        if root is None: return result
        result.append(root.val)

        # Left Boundry excluding leaf.
        curr = root.left
        while curr:
            if curr.left or curr.right:
                result.append(curr.val)
            if curr.left: curr = curr.left
            else: curr = curr.right
        
        # Leaf Nodes.
        curr = root
        stack = [curr]
        # Run loop till stack gets empty.
        while len(stack) > 0:
            # print the root node.
            node = stack.pop()
            if node != root and node.left is None and node.right is None:
                result.append(node.val)

            # push the right node first into stack so, it pop out later.
            if node.right is not None: stack.append(node.right)
            if node.left is not None: stack.append(node.left)

        # Right Boundry excluding leaf.
        curr = root.right
        tmp = []
        while curr:
            if curr.left or curr.right:
                tmp.append(curr.val)
            if curr.right: curr = curr.right
            else: curr = curr.left
        for i in range(len(tmp)-1, -1, -1):
            result.append(tmp[i])
        return result
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        return self.boundry_traversal(root)

"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/

Reference:
https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/basic_binary_tree.py
https://gist.github.com/jtribble/e5bcfc16b82a2547c22fc39877e81217
"""

# import sys
from dataclasses import dataclass
from typing import List, Optional
from collections import defaultdict  # , OrderedDict


@dataclass
class Node:
    """Dataclass represing node of the tree.
    """
    data: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None

# Create node
# node = Node(val, None, None)


class BinaryTree:
    """BinaryTree data structure.
    """

    def __init__(self) -> None:
        self.root: Optional['Node'] = None

    def __str__(self) -> str:
        tree_str = f"{self.root.data}"
        tree_str += '('
        if self.root.left is not None:
            tree_str += str(self.root.left)
        tree_str += ')('
        if self.root.right is not None:
            tree_str += str(self.root.right)
        tree_str += ')'
        return tree_str

    def display(self, root: Node | None) -> None:
        """display string of lelemnt of tree.

        Args:
            root (Node | None): Pass the root node of the tree.
        """
        if root is not None:
            self.display(root.left)
            print(root.data)
            self.display(root.right)

    def depth_of_tree(self, root: Node | None) -> int:
        """Recursive way to find height of the binary tree.

        Args:
            root (Node | None): Pass the root node of the tree.

        Returns:
            int: return the height of the tree.
        """
        return 1 + max(self.depth_of_tree(root.left), self.depth_of_tree(root.right)) if root else 0

    def depth_of_tree_iterative(self, root: Node | None) -> int:
        """Iterative way to find height of the binary tree.

        Args:
            root (Node | None): Pass the root node of the tree.

        Returns:
            int: return the height of the tree.
        """

        # Base Case
        if root is None:
            return 0
        queue = []
        queue.append(root)
        height = 0
        while True:
            # node_count(queue size) indicates number of nodes at current level
            node_count = len(queue)
            if node_count == 0:
                return height
            height += 1

            # Dequeue all nodes of current level and Enqueue all nodes of next level
            while node_count > 0:
                node = queue[0]
                queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                node_count -= 1

    def dfs(self, root: Node) -> Node:
        """Recursive Inorder traversal of binary tree.

        Args:
            tree (Node): Pass the root node of the tree.
        """
        if root is None:
            return
        yield from self.dfs(root.left)
        yield root
        yield from self.dfs(root.right)

    def dfs_iterative(self, root: Node) -> Node:
        """Iterative Inorder traversal of binary tree.

        Args:
            tree (BinaryTree): Pass the root node of the tree.
        """
        # create an empty stack and push root to it
        stack = []
        stack.append(root)
        curr = root
        while True:
            # Reach the left most Node of the current Node
            if curr is not None:
                # Place pointer to a tree node on the stack
                # before traversing the node's left subtree
                stack.append(curr)
                curr = curr.left
            # BackTrack from the empty subtree and visit the Node
            # at the top of the stack; however, if the stack is
            # empty you are done
            else:
                if len(stack) == 0:
                    return
                curr = stack.pop()
                yield curr  # print(curr.data, end=" ")
                # We have visited the node and its left
                # subtree. Now, it's right subtree's turn
                curr = curr.right

    def bfs(self, root: Node):
        """BFS or Level Order Traversal

        Args:
            tree (Node):
        """
        queue = []
        queue.append(root)
        while len(queue) > 0:
            curr = queue.pop(0)
            yield curr
            # print(curr.data)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)

    def inorder(self, root: Node) -> Node:
        """Inorder Traversal: Left-Root-Right
        """
        return self.dfs(root)

    def preorder(self, root: Node) -> Node:
        """Preorder Traversal: Root-Left-Right
        Recursive way.
        """
        if not root:
            return
        yield root  # print(root.data, end=" ")
        yield from self.preorder(root.left)
        yield from self.preorder(root.right)

    def preorder_iterative(self, root: Node) -> None:
        """Preorder Traversal: Root-Left-Right
        Iteraive way.
        """
        # create an empty stack and push root to it
        stack = []
        stack.append(root)
        # Run loop till stack gets empty.
        while len(stack) > 0:
            # print the root node.
            node = stack.pop()
            yield node  # print(node.data, end=" ")
            # push the right node first into stack so, it pop out later.
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

    def postorder(self, root: Node) -> None:
        """Postorder Traversal: Left-Right-Root
        Recursive Way.
        """
        if not root:
            return
        yield from self.postorder(root.left)
        yield from self.postorder(root.right)
        yield root  # print(root.data, end=" ")

    def postorder_iterative(self, root: Node) -> None:
        """Postorder Traversal: Left-Right-Root
        Iterative Way.
        """
        # create an empty stack and push root to it
        stack = []
        curr = root
        if not curr or len(stack) > 0:
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack[-1].right
            if temp is None:
                temp = stack.pop()
                yield temp  # print(temp.data, end=" ")
                while len(stack) > 0 and temp == stack[-1].right:
                    temp = stack.pop()
                    yield temp  # print(temp.data, end=" ")
            else:
                curr = temp

    def all_traversal(self, root: Node) -> None:
        """All Traversal: 
            1. Left-Root-Right
            2. Root-Left-Right
            3. Left-Right-Root
        Iterative Way.
        """
        pre, inn, post = [], [], []
        stack = []

        # Push root node of the tree into the stack
        stack.append([root, 1])

        while len(stack) > 0:
            top = stack[-1]
            # If the status of top node of the stack is 1
            if top[1] == 1:
                # Update the status of top node
                stack[-1][1] += 1
                # Insert the current node into preorder, pre[]
                pre.append(top[0].data)
                # If left child is not NULL
                if top[0].left:
                    # Insert the left subtree with status code 1
                    top.append([top[0].left, 1])

            # If the status of top node of the stack is 2
            elif top[1] == 2:
                # Update the status of top node
                stack[-1][1] += 1
                # Insert the current node in inorder, in[]
                inn.append(top[0].data)
                # If right child is not NULL
                if top[0].right:
                    # Insert the right subtree into the stack with status code 1
                    stack.append([top[0].right, 1])

            # If the status of top node of the stack is 3
            else:
                # Push the current node in post[]
                post.append(top[0].data)
                # Pop the top node
                stack.pop()

        print("Preorder Traversal: ", end=" ")
        for i in pre:
            print(i, end=" ")
        print()

        print("Inorder Traversal: ", end=" ")
        for i in inn:
            print(i, end=" ")
        print()

        print("Postorder Traversal: ", end=" ")
        for i in post:
            print(i, end=" ")
        print()

    def is_full_binary_tree(self, root: Node) -> bool:
        """Full Binary Tree: 
            Each & every node either has 0 or 2 children.
        """
        if root is None:
            return True
        if root.left and root.right:
            return self.is_full_binary_tree(root.left) and self.is_full_binary_tree(root.right)
        else:
            return not root.left and not root.right

    def is_complete_binary_tree(self, root: Node) -> bool:
        """Complete Binary Tree:
            All nodes except for the level before the last must have 2 children.
            All nodes in the last level are as far left as possible.
        """
        if root is None:
            return True

    def is_perfect_binary_tree(self, root: Node) -> bool:
        """Perfect Binary Tree:
            All interior nodes have two children and all leaves have the same depth.
        """
        if root is None:
            return True

    def is_balanced_binary_tree(self, root: Node) -> bool:
        """Balanced Binary Tree:
            The left and right subtrees of every node differ in height by no more than 1.
        """
        def height(root: Node) -> int:
            if root is None:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            if (left_height == -1 or right_height == -1):
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)
        return height(root) != -1

    def is_binary_search_tree(self, root: Node) -> bool:
        """Binary Search Tree:
            Ordered or Sorted Binary Tree
        """
        last_node = None  # type: Optional[BinaryTree]
        for node in self.dfs(root):
            if last_node and last_node.value >= node.value:
                return False
            last_node = node
        return True

    def diameter_brute_force(self, root: Node, maxx: int = 0) -> int:
        """Diameter of Binary Tree.
            The diameter of a binary tree is the length of the longest path between any two nodes in a tree. # pylint: disable=line-too-long
            This path may or may not pass through the root.
            The length of path between two nodes is represented by the number of edges between them.
        """
        if root is None:
            return 0
        left_height = self.depth_of_tree(root.left)
        right_height = self.depth_of_tree(root.right)

        # Return max of the following tree:
        # 1) Diameter of left subtree
        # 2) Diameter of right subtree
        # 3) Height of left subtree + height of right subtree
        maxx = max(maxx,
                   left_height + right_height,
                   self.diameter_brute_force(root.left, maxx),
                   self.diameter_brute_force(root.right, maxx))
        return maxx

    def diameter(self, root: Node) -> int:
        """Diameter of Binary Tree. Recusrsive Way. O(N) approach
        """
        maxx = 0

        def diameter1(root: Node) -> int:
            """height function.
            """
            nonlocal maxx
            if root is None:
                return 0
            left_height = diameter1(root.left)
            right_height = diameter1(root.right)
            maxx = max(maxx, left_height + right_height)
            return 1 + max(left_height, right_height)
        diameter1(root)
        return maxx

    def max_path_sum(self, root: Node) -> int:
        """max_path_sum of Binary Tree. Recusrsive Way. O(N) approach
        """
        maxpathsum = 0

        def max_path_sum1(root: Node) -> int:
            """height function.
            """
            nonlocal maxpathsum
            if root is None:
                return 0
            maxl = max_path_sum1(root.left)
            maxr = max_path_sum1(root.right)
            maxpathsum = max(maxpathsum,  root.data + maxl + maxr)
            return root.data + max(maxl, maxr)
        max_path_sum1(root)
        return maxpathsum

    def is_identical(self, first: Node, second: Node) -> bool:
        """_summary_
        """
        if not first or not second:
            return first == second
        return (first.data == second.data and
                self.is_identical(first.left, second.left) and
                self.is_identical(first.right, second.right))

    def zig_zag_level_order(self, root: Node) -> List[List[int]]:
        """_summary_
        """
        result = []
        if root is None:
            return result

        queue = []  # queue for adding each level of nodes.
        flag = True  # True denotes to left->right traversal.

        while len(queue) > 0:
            length = len(queue)
            row = [0]*length
            for i in range(length):
                node = queue.pop(0)
                ind = i if flag else length-i-1
                row[ind] = node.data
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            flag = not flag
            result.append(row)
        return result

    def boundry_traversal(self, root: Node) -> List[int]:
        """Boundery Traversal
            1. Left Boundry excluding leaf.
            2. Leaf Nodes.
            3. Right Boundry excluding leaf.
        """
        result = []
        if root is None:
            return result
        result.append(root.data)

        # Left Boundry excluding leaf.
        curr = root.left
        while curr:
            if curr.left or curr.right:
                result.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

        # Leaf Nodes.
        curr = root
        stack = [curr]
        # Run loop till stack gets empty.
        while len(stack) > 0:
            # print the root node.
            node = stack.pop()
            if curr.left or curr.right:
                result.append(curr.data)

            # push the right node first into stack so, it pop out later.
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        # Right Boundry excluding leaf.
        curr = root.right
        tmp = []
        while curr:
            if curr.left or curr.right:
                tmp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        for i in range(len(tmp)-1, -1, -1):
            result.append(tmp[i])
        return result

    def vertical_order_traversal(self, root: Node) -> List[List[int]]:
        """Vertical Order Traversal
        """
        # Base case
        result = []
        if root is None:
            return result

        nodes = defaultdict()
        # Create empty queue for level order traversal
        queue = [(root, 0, 0)]

        while len(queue) > 0:
            temp = queue.pop(0)
            node = temp[0]
            x_axis, y_axis = temp[1], temp[2]
            nodes[(x_axis, y_axis)].append(node.data)
            if node.left:
                queue.append((node.left, x_axis-1, y_axis+1))
            if node.right:
                queue.append((node.right, x_axis+1, y_axis+1))

        # for k,v in OrderedDict(sorted(data.keys()))
        for val in sorted(nodes).values():
            result.append(val)
        return result

    def topview(self, root: Node) -> List[int]:
        """Top View of Binary Tree
        """
        result = []
        if root is None:
            return result

        result_map = dict()
        queue = [(root, 0)]
        while len(queue) > 0:
            temp = queue.pop(0)
            node, x_axis = temp[0], temp[1]
            if x_axis not in result_map:
                result_map[x_axis] = node.data
            if node.left:
                queue.append((node.left, x_axis-1))
            if node.right:
                queue.append((node.right, x_axis+1))

        # for k,v in OrderedDict(sorted(data.keys()))
        for val in sorted(result_map).values():
            result.append(val)
        return result

    def bottomview(self, root: Node) -> List[int]:
        """Bottom View of Binary Tree
        """
        result = []
        if root is None:
            return result
        left_lst, right_lst = [], []

        queue = [(root, 0)]
        while len(queue) > 0:
            temp = queue.pop(0)
            node, x_axis = temp[0], temp[1]
            if x_axis >= 0:
                if x_axis < len(right_lst):
                    right_lst[x_axis] = node.data
                else:
                    right_lst.append(node.data)
            else:
                if (-1*x_axis)-1 < len(left_lst):
                    left_lst[(-1*x_axis)-1] = node.data
                else:
                    left_lst.append(node.data)
            # result_map[x_axis] = node.data # Overwrite value of map
            if node.left:
                queue.append((node.left, x_axis-1))
            if node.right:
                queue.append((node.right, x_axis+1))

        result = left_lst[::-1] + right_lst
        return result

    # ! CODE IS NOT DONE YET :(
    def leftview(self, root: Node) -> List[int]:
        """_summary_
        """
        result = []
        if root is None:
            return result
        return []

    # ! CODE IS NOT DONE YET :(
    def rightview(self, root: Node) -> List[int]:
        """_summary_
        """
        result = []
        if root is None:
            return result
        return []

    def printpath_iterative(self, root: Node, node: Node) -> List[int]:
        """Print Root to Node Path in Binary Tree
        """
        # create an empty stack and push root to it
        stack = []
        stack.append(root)
        curr = root
        while True:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                if len(stack) == 0 or curr.data == node.data:
                    break
                curr = stack.pop()
                curr = curr.right
        return stack

    def printpath(self, tree: Node, node: Node) -> List[int]:
        """_summary_
        """
        # create an empty stack and push root to it
        result = []
        if not tree:
            return result

        def getpath(curr: BinaryTree, result: List[int], node: BinaryTree) -> None:
            # Reached to leaf node and node not found.
            # return False and pop the value after if condition.
            if not curr:
                return False

            result.append(curr.data)
            # Retrn true id Node found.
            if curr.data == node.data:
                return True

            # Return true if any child has node available int there path.
            if getpath(curr.left, result, node) or getpath(curr.right, result, node):
                return True

            # Else pop the value from stack and return false.
            result.pop()
            return False

        curr = tree
        getpath(curr, result, node)
        return result

    def is_symmetric(self, root: Node) -> bool:
        """Check tree is symmetric or not.
        """
        if root is None:
            return True

        def symmetric(left: Node, right: Node) -> bool:
            if left is None or right is None:
                return left == right
            if left.data != right.data:
                return False
            return symmetric(left.left, right.right) and symmetric(left.right, right.left)

        return symmetric(root.left, root.right)

    def lca(self, root: Node, first: Node, second: Node) -> Node:
        """Return Lowest Common Ancestor(Parent) of both the ndes from tree.
        """
        if root is None or first == root or second == root:
            return root

        left = self.lca(root.left, first, second)
        right = self.lca(root.right, first, second)

        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root

    def max_width(self, root: Node) -> int:
        """Return Lowest Common Ancestor(Parent) of both the ndes from tree.
        """
        # Base case
        if root is None:
            return 0

        # Create empty queue for level order traversal
        queue = [(root, 1)]
        width = float('-inf')
        while len(queue) > 0:
            length = len(queue)
            first, last = float('inf'), float('-inf')
            for _ in range(length):
                temp = queue.pop(0)
                node, node_number = temp[0], temp[1]
                first = min(first, node_number)
                last = max(last, node_number)
                if node.left:
                    queue.append((node.left, 2*(node_number-1)+1))
                if node.right:
                    queue.append((node.right, 2*(node_number-1)+2))

            width = max(width, last-first+1)

        return width

    # TODO: SEARCH FOR MORE EFFICIENT APPROACH.
    def child_sum(self, root: Node) -> None:
        """ Convert BinaryTree into children sum property.
        """
        if root is None:
            return
        child = 0
        if root.left:
            child += root.left.data
        if root.right:
            child += root.right.data

        if child >= root.data:
            root.data = child
        else:
            if root.left:
                root.left.data = root.data
            if root.right:
                root.right.data = root.data

        self.child_sum(root.left)
        self.child_sum(root.right)

        total = 0
        if root.left:
            total += root.left.data
        if root.right:
            total += root.right.data
        if root.left or root.right:
            root.data = total

    # ! CODE IS NOT DONE YET :(
    def get_nodes_at_k_distance(self, root: Node, target: Node, distance: int) -> List[Node]:
        """Retruns all the Nodes which are at the K-distance from the target node.
        Approach 1:
            Find Node to root path.
            from node get the nodes which are k distance down.
            from the parent node get the nodes which are (k-1) distance down and not in path.
            do the same for other nodes in the path.
        Approach 2:
            Use BFS create parent link for each node.
            Move to Left, Right and Parent.
            Use Visited Hash for duplicate paths.
            Count distance at each point and return nodes.
        Approach 3: (OPTIMIZED)
            Use blocking node on retunrs way if path.
            it will save space.
            same as 1.
        """
        if root is None:
            return []
        return []

    # ! CODE IS NOT DONE YET :(
    def burn_time(self, root: Node, start: int) -> int:
        """Minimum time to burn a Tree starting from a node.
        Approach: Foreach node get 
            sum of 
                (the depth till the presententing node)
                    and 
                (height of opposite side of the tree)
        """
        if root is None:
            return 0

        left_h = self.burn_time(root.left, start)
        right_h = self.burn_time(root.right, start)

        return 1 + max(left_h, right_h)

    def construct_treefrom_pre_in(self, pre, in_):
        """Construct a binary tree from the given inputs.
        """
        def construct_tree1(pre, in_, pre_start, pre_end, in_start, in_end, in_map):
            if pre_start > pre_end or in_start > in_end:
                return None

            # Create root nodfe fot the subtree.
            root = Node(pre[0])

            # find the lcoation of the root node in the inorder traversal.
            # divide tree into two subtree based on inorder trversal.
            in_root = in_map[root.data]

            # number of elements in leftside of the root in inorder traversal
            # will be same number of element in preorder traversal after first(root) element.
            no_left = in_root-in_start

            root.left = construct_tree1(
                pre, in_, pre_start+1, pre_start+no_left, in_start, in_root-1, in_map)
            root.right = construct_tree1(
                pre, in_, pre_start+no_left+1, pre_end, in_root+1, in_end, in_map)

            # return the root element of the binary tree.
            return root

        in_map = defaultdict()
        for ind, node in enumerate(in_):
            in_map[node] = ind
        root = construct_tree1(pre, in_, 0, len(pre)-1, 0, len(in_)-1, in_map)
        return root

    def construct_tree_from_post_in(self, post, in_) -> Node:
        """Construct a binary tree from the given inputs.
        """
        def construct_tree1(post, in_, post_start, post_end, in_start, in_end, in_map):
            if post_start > post_end or in_start > in_end:
                return None

            # Create root nodfe fot the subtree.
            root = Node(post[-1])

            # find the lcoation of the root node in the inorder traversal.
            # divide tree into two subtree based on inorder trversal.
            in_root = in_map[root.data]

            # number of elements in leftside of the root in inorder traversal
            # will be same number of element in preorder traversal after first(root) element.
            no_left = in_root-in_start

            root.left = construct_tree1(
                post, in_, post_start, post_start+no_left-1, in_start, in_root-1, in_map)
            root.right = construct_tree1(
                post, in_, post_start+no_left, post_end-1, in_root+1, in_end, in_map)

            # return the root element of the binary tree.
            return root

        in_map = defaultdict()
        for ind, node in enumerate(in_):
            in_map[node] = ind
        root = construct_tree1(post, in_, 0, len(
            post)-1, 0, len(in_)-1, in_map)
        return root

    def inorder_morris_traversal(self, root: Node) -> Node:
        """The idea of Morris Traversal is based on Threaded Binary Tree. 
        In this traversal, we first create links to Inorder successor and print the data using these links, 
        and finally revert the changes to restore original tree.
        Time Complexity : O(n)
        Auxiliary Space: O(1)
        """
        curr = root
        while curr is not None:
            if curr.left is None:
                yield curr
                # inorder_list.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right is not None and prev.right != curr:
                    prev = prev.right
                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    yield curr
                    # inorder_list.append(curr.val)
                    curr = curr.right

    def preorder_morris_traversal(self, root: Node) -> Node:
        """Morris Traversal Preorder.
        """
        curr = root
        while curr is not None:
            yield curr
            if curr.left is None:
                curr = curr.right
            else:
                prev = curr.left
                while prev.right is not None and prev.right != curr:
                    prev = prev.right
                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    curr = curr.right

    # ! CODE IS NOT DONE YET :(
    def flatten(self, root: Node):
        """Flatten a binary tree.
        """
        # def flattenTree(node: Node):
        #     """
        #     Flatten Tree
        #     """
        #     if node is None:
        #         return None
        #     if not node.left and not node.right:
        #         return node

        #     leftTail = flattenTree(node.left)
        #     rightTail = flattenTree(node.right)

        #     if leftTail:
        #         leftTail.right = node.right
        #         node.right = node.left
        #         node.left = None

        #     return rightTail if rightTail else leftTail
        # return flattenTree(root)

        # Morris Traversal
        if not root:
            return None
        curr = root
        while curr:
            if curr.left:
                # Find the rightmost node
                rightmost = curr.left
                while rightmost.right:
                    rightmost = rightmost.right
                # rewire the connections
                rightmost.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
        return root

        # >>>>>> Binary Search Tree functions ftarts

    def insert(self, root: Node, node: Node) -> Node:
        """Insert element into binary tree.
            Returns the root node of the tree after inserting value.
        """
        if root is None:
            return node
        if root.data < node.data:
            root.right = self.insert(root.right, node)
        elif root.data > node.data:
            root.left = self.insert(root.left, node)
        else:
            print("Element already present")
        return root

    def find(self, root: Node, data: int) -> Node:
        """Find the node if it exist in the tree.
        """
        curr = root
        while curr is not None and curr.data != data:
            curr = curr.left if data < curr.data else curr.right
        return curr

    def find_parent(self, root: Node, data: int) -> Node:
        """Find the node if it exist in the tree.
        """
        if root is None:
            return None
        curr = root
        # Check if node does not have any child return None
        if curr.left is not None and curr.right is not None:
            return None
        # Check for left value and right value. if match return current node.
        if (curr.left and curr.left.data == data) or (curr.right and curr.right.data == data):
            return curr
        # compare values to decide where to go left/right.
        if data < curr.data:
            return self.find_parent(curr.left, data)
        if data > curr.data:
            return self.find_parent(curr.right, data)

    def successor(self, root: Node, data: int) -> Node:
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
                if (root.data < data):
                    root = root.right
                elif (root.data > data):
                    succ, root = root, root.left
                else:
                    break
            return succ

        while node.left:
            node = node.left
        return node

    def ceil(self, root: Node, data: int) -> Node:
        """the smallest integer greater than or equal to a given number. 
        """
        ceil = -1
        while root:
            if data > root.data:
                root = root.right
            else:
                ceil = data
                root = root.left
                if root.data == data:
                    return ceil
        return ceil

    def predecessor(self, root: Node, data: int) -> Node:
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
                if (root.data < data):
                    pred, root = root, root.right
                elif (root.data > data):
                    root = root.left
                else:
                    break
            return pred

        while node.right:
            node = node.right
        return node

    def floor(self, root: Node, data: int) -> Node:
        """the greater integer lesser than or equal to a given number. 
        """
        floor = -1
        while root:
            if data > root.data:
                floor = data
                root = root.right
                if root.data == data:
                    return floor
            else:
                root = root.left
        return floor

    def delete(self, root: Node, data: int) -> Node:
        """Delete Node from the BST.
        """
        if root is None:
            return root

        if root.data == data:
            # if node has no child. Remove connection from parent node.
            if root.left is None and root.right is None:
                del root
                return None

            # if node has only one child. connect parent node with child node.
            if root.left is None:
                temp = root.right
                del root
                return temp
            elif root.right is None:
                temp = root.left
                del root
                return temp

            # if node has two child. replace node with inorder predecessor/successor.
            else:
                # right Min value.
                r_min = root.right
                while root.left is not None:
                    r_min = root.left
                # left Max value.
                # l_max = root.left
                # while root.right is not None:
                #     l_max = root.right
                root.data = r_min.data
                root.right = self.delete(root.right, r_min.data)
                return root

        elif root.data < data:
            root.left = self.delete(root.left, data)
            return root

        else:  # root.data > data
            root.right = self.delete(root.right, data)
            return root

    # ! CODE IS NOT DONE YET :(
    def construct_bst_from_pre(self, pre):
        return
    # <<<<<< Binary Search Tree functions ends

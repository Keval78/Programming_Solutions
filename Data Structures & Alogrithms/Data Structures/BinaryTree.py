'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
'''
Reference: https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/basic_binary_tree.py
'''
    

class BinaryTree():
    class BinaryTree:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.left: BinaryTree | None = None
        self.right: BinaryTree | None = None

    # def insertLeft(self, newNode) -> None:
    #     if self.left == None:
    #         self.left = BinaryTree(newNode)
    #     else:
    #         t = BinaryTree(newNode)
    #         t.left = self.left
    #         self.left = t

    # def insertRight(self,newNode) -> None:
    #     if self.right == None:
    #         self.right = BinaryTree(newNode)
    #     else:
    #         t = BinaryTree(newNode)
    #         t.right = self.right
    #         self.right = t

    def __str__(self):
        s = f"{self.data}"
        s += '('
        if self.left != None:
            s += str(self.left)
        s += ')('
        if self.right != None:
            s += str(self.right)
        s += ')'
        return s
    
    def display(tree: BinaryTree | None) -> None:
    if tree:
        self.display(tree.left)
        print(tree.data)
        self.display(tree.right)
    
    def depth_of_tree(tree: BinaryTree | None) -> int:
        return 1 + max(self.depth_of_tree(tree.left), self.depth_of_tree(tree.right)) if tree else 0
    
    def depth_of_tree_iterative(tree: BinaryTree | None) -> int:
        # Base Case
        if tree is None: return 0
        queue = []
        queue.append(tree)
        height = 0
        while(True):
            # node_count(queue size) indicates number of nodes at current level
            node_count = len(queue)
            if node_count == 0: return height
            height += 1

            # Dequeue all nodes of current level and Enqueue all nodes of next level
            while(node_count > 0):
                node = queue[0]
                queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                node_count -= 1


    # DFS
    def dfs(tree: BinarTree) -> None:
        if is not tree:
            return
        self.dfs(tree.left)
        print(tree.data, end=" ")
        self.dfs(tree.right)
    
    def dfs_iterative(tree: BinarTree) -> None:
        # create an empty stack and push root to it
        stack = []
        stack.append(tree)
        curr = tree
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
                print(curr.data, end=" ")
                # We have visited the node and its left
                # subtree. Now, it's right subtree's turn
                curr = curr.right


    # BFS or Level Order Traversal
    def bfs(tree: BinaryTree):
        queue = []
        queue.append(tree)
        while len(queue) > 0:
            curr = queue.pop(0)
            print(curr.data)
            if curr.left is not None: queue.append(curr.left)
            if curr.right is not None: queue.append(curr.right)



    # Inorder Traversal: Left-Root-Right
    def inorder(tree: BinaryTree) -> None:
        return self.dfs(tree)
    


    # Preorder Traversal: Root-Left-Right
    def preorder(tree: BinaryTree) -> None:
        if is not tree:
            return
        print(tree.data, end=" ")
        self.preorder(tree.left)
        self.preorder(tree.right)
    
    def preorder_iterative(tree: BinaryTree) -> None:
        # create an empty stack and push root to it
        stack = []
        stack.append(tree)
        # Run loop till stack gets empty.
        while(len(stack) > 0):
            # print the root node.
            node = stack.pop()
            print (node.data, end=" ")
            # push the right node first into stack so, it pop out later.
            if node.right is not None: stack.append(node.right)
            if node.left is not None: stack.append(node.left)



    # Postorder Traversal: Left-Right-Root
    def postorder(tree: BinaryTree) -> None:
        if is not tree:
            return
        print(tree.data, end=" ")
        self.postorder(tree.right)
        self.postorder(tree.left)
    
    def postorder_iterative(tree: BinaryTree) -> None:
        # create an empty stack and push root to it
        stack = []
        curr = tree
        if not curr or len(stack)>0:
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack[-1].right
            if temp == None:
                temp = stack.pop()
                print(temp.data, end=" ")
                while len(stack)>0 and temp=stack[-1].right:
                    temp = stack.pop()
                    print(temp.data, end=" ")
            else:
                curr = temp
    
    def all_traversal(tree: BinaryTree) -> None:
        pre, inn, post = [], [], []
        stack = []
 
        # Push root node of the tree into the stack
        stack.append([tree, 1])

        while (len(s) > 0):
            p = s[-1]
            # If the status of top node of the stack is 1
            if (p[1] == 1):
                # Update the status of top node
                s[-1][1] += 1
                # Insert the current node into preorder, pre[]
                pre.append(p[0].data)
                # If left child is not NULL
                if (p[0].left):
                    # Insert the left subtree with status code 1
                    s.append([p[0].left, 1]) 
            
            # If the status of top node of the stack is 2
            elif (p[1] == 2):
                # Update the status of top node
                s[-1][1] += 1
                # Insert the current node in inorder, in[]
                inn.append(p[0].data)
                # If right child is not NULL
                if (p[0].right):
                    # Insert the right subtree into the stack with status code 1
                    s.append([p[0].right, 1])
            
            # If the status of top node of the stack is 3
            else:
                # Push the current node in post[]
                post.append(p[0].data)
                # Pop the top node
                del s[-1]
        
        print("Preorder Traversal: ",end=" ")
        for i in pre: print(i,end=" ")
        print()
    
        print("Inorder Traversal: ",end=" ")
        for i in inn: print(i,end=" ")
        print()
    
        print("Postorder Traversal: ",end=" ")
        for i in post: print(i,end=" ")
        print()



    # Full Binary Tree:
    # Each & every node either has 0 or 2 children.
    def is_full_binary_tree(tree: BinaryTree) -> bool:
        if not tree: return True
        if tree.left and tree.right:
            return is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)
        else:
            return not tree.left and not tree.right
    
    # Complete Binary Tree:
    # All nodes except for the level before the last must have 2 children.
    # All nodes in the last level are as far left as possible.
    def is_complete_binary_tree(tree: BinaryTree) -> bool:
        if not tree: return True
    
    # Perfect Binary Tree: 
    # All interior nodes have two children and all leaves have the same depth.
    def is_perfect_binary_tree(tree: BinaryTree) -> bool:
        if not tree: return True

    # Balanced Binary Tree: 
    # The left and right subtrees of every node differ in height by no more than 1.
    def is_balanced_binary_tree(tree: BinaryTree) -> bool:
        def height(tree: BinaryTree) -> int:
            if not tree: return 0
            lh = self.is_balanced_binary_tree(tree.left)
            rh = self.is_balanced_binary_tree(tree.right)
            if (lh==-1 or rh==-1): return -1
            if abs(lh-rh) > 1: return -1
            return 1 + max(lh, rh)
        return height(tree) !== -1
    
    # Diameter of Binary Tree.
    # The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    # This path may or may not pass through the root.
    # The length of path between two nodes is represented by the number of edges between them.
    def diameter_brute_force(tree: BinaryTree, maxx: int = 0) -> int:
        if not tree: return 0
        lh = self.depth_of_tree(tree.left)
        rh = self.depth_of_tree(tree.right)

         # Return max of the following tree:
        # 1) Diameter of left subtree
        # 2) Diameter of right subtree
        # 3) Height of left subtree + height of right subtree
        maxx = max(maxx, lh+rh)
        maxx = max(maxx, self.diameter_brute_force(tree.left, maxx))
        maxx = max(maxx, self.diameter_brute_force(tree.right, maxx))
        return maxx
    
    def diameter(tree: BinaryTree) -> int:
        maxx = 0
            def diameter1(tree: BinaryTree) -> int:
            if not tree: return 0
            lh = self.diameter1(tree.left)
            rh = self.diameter1(tree.right)
            maxx = max(maxx, lh+rh)
            return 1 + max(lh, rh)
        return maxx
    
    def max_path_sum(tree: BinaryTree, maxpathsum: int = 0) -> int:
        maxpathsum = 0
        def max_path_sum1(tree: BinaryTree) -> int:
            if not tree: return 0
            maxl = self.max_path_sum1(tree.left)
            maxr = self.max_path_sum1(tree.right)
            maxpathsum = max(maxpathsum,  tree.data + maxl + maxr)
            return tree.data + max(maxl, maxr)
        return maxpathsum
    
    def is_identical(p: BinaryTree, q: BinarTree) -> bool:
        if not p or not q:
            return p==q
        return p.data==q.data and is_identical(p.left, q.left) and is_identical(p.right, q.right)
    
    def zig_zag_level_order(tree: BinaryTree) -> List[List[int]]:
        result = []
        if not tree: return result
        
        queue = [] # queue for adding each level of nodes.
        flag = True # True denotes to left->right traversal.

        while len(queue) > 0:
            length = len(queue)
            row = [0]*length
            for i in range(length):
                node = queue.pop(0)
                ind = i if flag else length-i-1
                row[ind] = node.data
                if node.left: queue.push(node.left)
                if node.right: queue.push(node.right)
            
            flag = not flag
            result.append(row)
        return result


    # Boundery Traversal
    # 1. Left Boundry excluding leaf.
    # 2. Leaf Nodes.
    # 3. Right Boundry excluding leaf.
    def boundry_traversal(tree: BinaryTree) -> List[int]:
        result = []
        if not tree: return result
        result.append(tree.data)
        
        # Left Boundry excluding leaf.
        curr = tree.left
        while curr:
            if curr.left or curr.right: result.append[curr.data]
            if curr.left: curr = curr.left
            else: curr = curr.right

        # Leaf Nodes.
        curr = tree
        stack = [curr]
        # Run loop till stack gets empty.
        while(len(stack) > 0):
            # print the root node.
            node = stack.pop()
            if curr.left or curr.right:
                result.append(curr.data)
            
            # push the right node first into stack so, it pop out later.
            if node.right is not None: stack.append(node.right)
            if node.left is not None: stack.append(node.left)


        # Right Boundry excluding leaf.
        curr = tree.right
        tmp = []
        while curr:
            if curr.left or curr.right: tmp.append[curr.data]
            if curr.right: curr = curr.right
            else: curr = curr.left
        for i in range(len(tmp)-1, -1, -1):
            result.append[tmp[i]]
    

    # * ! Error 
    def vertical_order_traversal(tree: BinarTree) -> List[List[int]]
        
        # Base case
        if tree is None: return

        # Create empty queue for level order traversal
        queue = [tree]
        x_axis, y_axis = 0, 0

        # create a map to store nodes at a particular
        # horizontal distance
        result_map = {}
        
        return []
    



    






    

















    # def find(tree: BinaryTree, data: int) -> BinaryTree:
    #     curr = tree
    #     while curr:
    #         if data < curr.data:
    #             if (curr.left == None):
    #                 return curr
    #             curr = curr.left
    #         elif (data > curr.data):
    #             if (curr.right == None):
    #                 return curr
    #             curr = curr.right
    #         else:
    #             return curr
    #     return None
    
    # def put(tree: BinaryTree, data: int) -> None:
    #     leaf = BinaryTree(data)
    #     if not tree:
    #         tree = leaf
    #     else:
    #         parent = find(data)
    #         if data < parent.data:
    #             parent.left = leaf
    #         else:
    #             parent.right = leaf
    
    def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
        successor = None
        while is not tree:
            if node.data >= tree.data:
                tree = tree.right
            else:
                successor = tree
                tree = tree.left
        return successor


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


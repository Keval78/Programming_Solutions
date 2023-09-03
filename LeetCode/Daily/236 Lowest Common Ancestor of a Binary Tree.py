'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeAncestor:
    def __init__(self, root, nodes, height):
        n = nodes
        k = height.bit_length() + 1

        bl_map = {}
        # Store parent in Binary Lifting
        depth = [0 for i in range(n)]
        bl_table = [[None for _ in range(n)] for _ in range(k)]

        que = deque([(None, root)])
        ind = 0
        while que:
            parent, node = que.popleft()
            bl_table[0][ind] = parent
            if parent is not None:
                depth[ind] = depth[bl_map[parent.val]] + 1
            bl_map[node.val] = ind
            ind += 1

            if node.left:
                que.append((node, node.left))
            if node.right:
                que.append((node, node.right))

        for i in range(1, k):
            for j in range(n):
                pnode = bl_table[i-1][j]
                if pnode is None:
                    ppnode = None
                else:
                    ppnode = bl_table[i-1][bl_map[pnode.val]]
                bl_table[i][j] = ppnode

        # print([k for k, val in sorted(bl_map.items(), key = lambda x:x[1])])
        # for b in bl_table:
        #     row = []
        #     for x in b:
        #         row.append(x.val if x else -1)
        #     print(row)
        #     print(bl_map)
        # print(depth)

        self.bl_map = bl_map
        self.bl_table = bl_table
        self.depth = depth
        self.k = k

    def getKthAncestor(self, node, k):
        # walk on binary of k.
        # print(node.val, k)
        j = 0
        while k > 0:
            # print(k, j, k&1, self.bl_table[j][node])
            if k & 1:
                node = self.bl_table[j][self.bl_map[node.val]]
            j += 1
            k = k >> 1
        return node

    def LCA(self, p, q):
        if (self.depth[self.bl_map[p.val]] < self.depth[self.bl_map[q.val]]):
            p, q = q, p

        # Make depth of p & q same.
        k = self.depth[self.bl_map[p.val]] - self.depth[self.bl_map[q.val]]
        p = self.getKthAncestor(p, k)

        # LCA of p & q; where depth of p & q is same.
        if p == q:
            return p

        for j in range(self.k-1, -1, -1):
            if self.bl_table[j][self.bl_map[p.val]] != self.bl_table[j][self.bl_map[q.val]]:
                p = self.bl_table[j][self.bl_map[p.val]]
                q = self.bl_table[j][self.bl_map[q.val]]

        return self.bl_table[0][self.bl_map[p.val]]


class Solution:
    def get_nodes_and_height(self, root: 'TreeNode'):
        if root is None:
            return (0, 0)

        lnodes, lheight = self.get_nodes_and_height(root.left)
        rnodes, rheight = self.get_nodes_and_height(root.right)
        return (1+lnodes+rnodes, 1+max(lheight, rheight))

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        nodes, height = self.get_nodes_and_height(root)
        # print(nodes, height)

        ta = TreeAncestor(root, nodes, height)

        lca = ta.LCA(p, q)
        return lca

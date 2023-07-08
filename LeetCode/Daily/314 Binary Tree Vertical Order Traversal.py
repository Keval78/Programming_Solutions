"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from collections import deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        que = deque()
        que.append((root,0))
        nodes = {}
        while len(que) > 0:
            for i in range(len(que)):
                node, level = que.popleft()
                if level in nodes:
                    nodes[level].append(node.val)
                else:
                    nodes[level] = [node.val]
                if node.left:
                    que.append((node.left, level-1))
                if node.right:
                    que.append((node.right, level+1))

        #print(nodes)
        return [nodes[key] for key in sorted(nodes)]

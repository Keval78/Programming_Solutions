'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from collections import defaultdict 

def main():
    class Solution:
        def countComponents(self, n: int, edges: List[List[int]]) -> int:
            # adjList = defaultdict(list)
            # visited = [False for i in range(n)]
            # cmpnts = 0
            # for edge in edges:
            #     i, j = edge
            #     adjList[i].append(j)
            #     adjList[j].append(i)
            # for vertice in range(n):
            #     if not visited[vertice]:
            #         cmpnts += 1
            #         visited[vertice] = True
            #         stack = [vertice]
            #         while stack:
            #             temp = stack.pop()
            #             for new_vertex in adjList[temp]:
            #                 if not visited[new_vertex]:
            #                     stack.append(new_vertex)
            #                     visited[new_vertex] = True
                        
            # return cmpnts

            # Disjoint Set Solution:
            p = [i for i in range(n)]
            def find(v):
                if p[v] != v: 
                    p[v] = find(p[v])
                return p[v]
            for e in edges:
                v, w = map(find, e)
                p[v] = w
                n -= v != w
            return n

    


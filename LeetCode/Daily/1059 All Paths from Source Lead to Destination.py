'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
def main():
    class Solution:
        def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
            def dfs_loop_check(graph, node, dest, states):
                if states[node] != None:
                    return not states[node]

                if len(graph[node]) == 0:
                    return node == dest
                
                #Intially set it as loop true.
                states[node] = True
                for next_node in graph[node]:            
                    if not dfs_loop_check(graph, next_node, dest, states):
                        return False
                
                #if do not detect loop mark it False
                states[node] = False
                return True
            
            graph = [[] for i in range(n)]
            for edge in edges:
                i, j = edge
                graph[i].append(j)
            return dfs_loop_check(graph, source, destination, states=[None]*n)




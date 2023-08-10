class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = [False]*len(graph)
        visit = [False]*len(graph)
        path_visit = [False]*len(graph)
        def dfs_cycle(node, graph, visit, path_visit, safe):
            visit[node] = path_visit[node] = True

            for adj in graph[node]:
                if not visit[adj]:
                    if dfs_cycle(adj, graph, visit, path_visit, safe):
                        return True
                elif path_visit[adj]:
                    return True
            
            safe[node] = True
            path_visit[node] = False
            return False
        
        for i in range(len(graph)):
            if not visit[i]:
                dfs_cycle(i, graph, visit, path_visit, safe)

        return [i for i in range(len(safe)) if safe[i]]

        
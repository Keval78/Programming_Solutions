class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if it is possible to write topological sorting. then we can perform tasks.
        indegrees = [0 for i in range(numCourses)]
        edge_map = defaultdict(list)
        for prq in prerequisites:
            indegrees[prq[1]] += 1
            edge_map[prq[0]].append(prq[1])
        
        que = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                que.append(i)
        
        tp_sorting = []
        while len(que):
            node = que.popleft()
            tp_sorting.append(node)
            for adj in edge_map[node]:
                indegrees[adj] -= 1
                if indegrees[adj] == 0:
                    que.append(adj)
        
        return True if len(tp_sorting)==numCourses else False

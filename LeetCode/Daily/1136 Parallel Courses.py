class Solution:
    def minimumSemesters(self, n, relations):
        indegrees = [0]*(n+1)
        edge_map = [[] for i in range(n+1)]

        for u, v in relations:
            edge_map[u].append(v)
            indegrees[v] += 1
        
        maxi = 0
        que = deque([(i,1) for i in range(1,n+1) if indegrees[i]==0])
        topo = []
        while que:
            u, l = que.popleft()
            topo.append(u)
            maxi = max(maxi, l)
            for v in edge_map[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    que.append((v, l+1))

        if len(topo) != n: return -1
        return maxi
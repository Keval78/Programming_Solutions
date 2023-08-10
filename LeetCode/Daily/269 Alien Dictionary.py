class Solution:
    def alienOrder(self, words: List[str]) -> str:
        edge_map = defaultdict(list)
        indegrees = Counter({c:0 for word in words for c in word})
        for x, y in pairwise(words):
            for a, b in zip(x,y):
                if a!=b:
                    edge_map[a].append(b)
                    indegrees[b] += 1
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(y) < len(x): return ""
                    
        
        que = deque([c for c in indegrees if indegrees[c] == 0])

        tp_sorting = []
        while len(que):
            node = que.popleft()
            tp_sorting.append(node)
            for adj in edge_map[node]:
                indegrees[adj] -= 1
                if indegrees[adj] == 0:
                    que.append(adj)
        
        return "".join(tp_sorting) if len(tp_sorting)==len(indegrees) else ""
from collections import defaultdict
from typing import List
from heapq import heappush, heappop


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # edge_map = defaultdict(list)
        # for i, edge in enumerate(edges):
        #     x, y = edge
        #     edge_map[x].append((y, succProb[i]))
        #     edge_map[y].append((x, succProb[i]))
        # # print(edge_map)

        # # Implement Dijksstra with maxheap.
        # min_prob = [0] * n
        # min_prob[start_node] = -1
        # heap = [(-1, start_node)]
        # ans = 0
        # while heap:
        #     prob, u  = heappop(heap)
        #     if u == end_node: return -min_prob[u]
        #     for v, path_prob  in edge_map[u]:
        #         if min_prob[v] > prob * path_prob:
        #             min_prob[v] = prob * path_prob
        #             heappush(heap, (min_prob[v], v))
        # return 0

        edge_map = defaultdict(list)
        for i, edge in enumerate(edges):
            x, y = edge
            edge_map[x].append((y, succProb[i]))
            edge_map[y].append((x, succProb[i]))
        # print(edge_map)

        # Implement Dijksstra with maxheap.
        visited = set()
        heap = [(-1, start_node)]
        while heap:
            # print(heap)
            prob, u = heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            if u == end_node:
                return -prob
            for v, next_prob in edge_map[u]:
                if v in visited:
                    continue
                heappush(heap, (prob*next_prob, v))
        return 0

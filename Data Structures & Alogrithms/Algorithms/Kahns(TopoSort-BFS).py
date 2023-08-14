"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/

Reference:
https://github.com/TheAlgorithms/Python/blob/master/graphs/kahns_algorithm_topo.py
"""
from collections import deque


def topological_sort(graph):
    """
    Kahn's Algorithm is used to find Topological ordering of Directed Acyclic Graph
    using BFS
    """
    n = len(graph)
    indegrees = [0] * n
    tp_sorting = []

    for values in graph.values():
        for i in values:
            indegrees[i] += 1

    que = deque([i for i in range(len(indegrees)) if indegrees[i] == 0])

    while len(que):
        node = que.popleft()
        tp_sorting.append(node)
        for adj in graph[node]:
            indegrees[adj] -= 1
            if indegrees[adj] == 0:
                que.append(adj)

    if len(tp_sorting) != n:
        print("Cycle exists")
    else:
        print(tp_sorting)


# Adjacency List of Graph
graph = {0: [1, 2], 1: [3], 2: [3], 3: [4, 5], 4: [], 5: []}
topological_sort(graph)

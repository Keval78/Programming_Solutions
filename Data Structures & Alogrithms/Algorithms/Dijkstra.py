
"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/

Reference:
https://github.com/TheAlgorithms/Python/blob/master/graphs/dijkstra.py
"""

import heapq
from typing import List, Tuple, Dict


def dijkstra(graph: Dict[str, List[Tuple[str, int]]], start: str, end: str) -> int:
    """
    Args:
        graph (dict): The graph represented as a dictionary of nodes and their neighbors with weights.
        start (str): The starting vertex.
        end (str): The ending vertex.

    Returns:
        int: The cost of the shortest path between start and end vertices, or -1 if no path exists.
    """
    heap = [(0, start)]  # cost from start node,end node
    visited = set()
    while heap:
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if u == end:
            return cost
        for v, next_cost in graph[u]:
            if v in visited:
                continue
            total = cost + next_cost
            heapq.heappush(heap, (total, v))
    return -1


G = {
    "A": [("B", 2), ("C", 5)],
    "B": [("A", 2), ("D", 3), ("E", 1), ("F", 1)],
    "C": [("A", 5), ("F", 3)],
    "D": [("B", 3)],
    "E": [("B", 4), ("F", 3)],
    "F": [("C", 3), ("E", 3)],
}

"""
>>> dijkstra(G, "E", "C")
6
>>> dijkstra(G2, "E", "F")
3
>>> dijkstra(G3, "E", "F")
3
"""
short_distance = dijkstra(G, "E", "C")
print(short_distance)  # E -- 3 --> F -- 3 --> C == 6

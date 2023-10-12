"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/

Reference:
https://codereview.stackexchange.com/questions/235898/speeding-up-dijkstras-algorithm
https://codereview.stackexchange.com/users/100620/ajneufeld
https://stackoverflow.com/users/3690024/ajneufeld
"""

from math import inf
from heapq import heappush, heappop
from typing import Any, Dict, List, Tuple, Union

Node = Any
Distance = float
Edges = Dict[Node, Distance]
Graph = Dict[Node, Edges]


def dijkstra(graph: Graph, start: Node, goal: Node) -> Tuple[Distance, List[Node]]:
    """
    Find the shortest distance between two nodes in a graph, and the path that produces that distance.
    The graph is defined as a mapping from Nodes to a Map of nodes which can be directly reached from that node, and the corresponding distance.

    Returns:
        A tuple containing
            - the distance between the start and goal nodes
            - the path as a list of nodes from the start to goal.

    If no path can be found, the distance is returned as infinite, and the path is an empty list.
    """
    shortest_distance: Dict[Node, Distance] = {}
    predecessor: Dict[Node, Union[Node, None]] = {}
    heap: List[Tuple[Distance, Node, Union[Node, None]]] = []

    heappush(heap, (0, start, None))

    while heap:
        distance, node, previous = heappop(heap)
        if node in shortest_distance:
            continue
        shortest_distance[node] = distance
        predecessor[node] = previous

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = predecessor[node]
            return distance, path[::-1]

        for successor, dist in graph[node].items():
            heappush(heap, (distance + dist, successor, node))

    # If no path is found
    return inf, []


if __name__ == '__main__':
    graph_main: Graph = {
        'a': {'b': 3, 'c': 4, 'd': 7},
        'b': {'c': 1, 'f': 5},
        'c': {'f': 6, 'd': 2},
        'd': {'e': 3, 'g': 6},
        'e': {'g': 3, 'h': 4},
        'f': {'e': 1, 'h': 8},
        'g': {'h': 2},
        'h': {'g': 2}
    }

    total_distance, full_path = dijkstra(graph_main, 'a', 'e')
    if total_distance == inf:
        print("No path")
    else:
        print(f"Distance = {total_distance}, path = {full_path}")

"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/

Reference:
https://github.com/TheAlgorithms/Python/blob/master/graphs/basic_graphs.py
"""


# import sys
from dataclasses import dataclass, field
from typing import Set, Dict, List, Optional
from collections import deque  # , defaultdict


@dataclass
class Vertex:
    """Dataclass represing vertex of the Graph.
    The @dataclass decorator is used to automatically generate common methods such as __init__, __repr__, and others, based on the class attributes. 
    This simplifies the process of creating instances of the Vertex class and provides a readable representation when printing the objects.
    """
    val: int
    adjacent: Dict[int, int] = field(default_factory=dict)

    def __str__(self) -> str:
        return str(self.val) + ' adjacent: ' + str([x.val for x in self.adjacent])

    def __hash__(self):
        return hash(self.val)

    def add_neighbor(self, neighbor, weight: int = 0, undirected: bool = True) -> None:
        """Add Neighbour for Undirected Graph.
        Args:
            neighbor (Vertex): Object of Neighbour Vertex.
            weight (int, optional): weight of the Edge.
        """
        self.adjacent[neighbor] = weight
        if undirected:
            neighbor.add_neighbor(self, weight, False)

    # def remove_neighbor(self, vertex: int) -> None:

    def get_connections(self) -> List[int]:
        """Returns all the neighbour of the Vertex.
        """
        return self.adjacent.keys()

    def get_id(self) -> int:
        """Return ID/Value of the Vertex.
        """
        return self.val

    def get_weight(self, neighbor) -> List[int]:
        """Returns weight of given neighbour
        """
        return self.adjacent[neighbor]


class Graph:
    """Graph data structure.
    """

    def __init__(self):
        # self.root: Optional['Node'] = None
        self.src: Optional['Vertex'] = None
        self.dest: Optional['Vertex'] = None
        self.vertices: Dict[int, 'Vertex'] = {}

    def __iter__(self):
        """Iterate through all vertices of graph
        """
        return iter(self.vertices.values())

    def add_vertex(self, val: int) -> Vertex:
        """Create & Add Vertex into the graph.
        """
        if val in self.vertices:
            return self.vertices[val]
        new_vertex = Vertex(val)
        self.vertices[val] = new_vertex
        return new_vertex

    def get_vertex(self, val: int) -> Vertex:
        """Get the vertex of the value.
        """
        return self.vertices[val] if val in self.vertices else None

    def add_undirected_edge(self, frm: int, to: int, weight: int = 0) -> None:
        """Add edge to Undirected Edge from->to with given weight.
        """
        self.add_vertex(frm)
        self.add_vertex(to)
        self.vertices[frm].add_neighbor(
            self.vertices[to], weight, undirected=True)

    def add_directed_edge(self, frm: int, to: int, weight=0) -> None:
        """Add edge to Directed Edge from->to with given weight.
        """
        self.add_vertex(frm)
        self.add_vertex(to)
        self.vertices[frm].add_neighbor(
            self.vertices[to], weight, undirected=False)

    def get_vertices(self) -> List[int]:
        """List of all vertices for the given Graph.
        """
        return self.vertices.keys()

    def dfs(self, frm, visited: Set[int]) -> Vertex:
        """Recusrsive DFS traversal of Graph.
        """
        visited.add(frm)
        # print(frm, visited)
        yield frm
        for vertex in self.get_vertex(frm).get_connections():
            if vertex.val not in visited:
                yield from self.dfs(vertex.val, visited)

    def dfs_iterative(self, frm: int) -> Vertex:
        """Iterative DFS traversal of Graph.
        """
        visited, stack = {frm}, [frm]
        yield frm
        while stack:
            for vertex in self.get_vertex(stack[-1]).get_connections():
                if vertex.val not in visited:
                    stack.append(vertex.val)
                    visited.add(vertex.val)
                    # print(vertex.val, stack)
                    yield vertex.val
                    break
            else:
                stack.pop()

    def bfs(self, frm: int) -> Vertex:
        """BFS traversal of Graph.
        """
        visited, que = {frm}, deque([frm])
        yield frm
        while que:
            for vertex in self.get_vertex(que.popleft()).get_connections():
                if vertex.val not in visited:
                    visited.add(vertex.val)
                    que.append(vertex.val)
                    yield vertex.val


if __name__ == '__main__':
    g = Graph()
    g.add_undirected_edge('a', 'b', 7)
    g.add_undirected_edge('a', 'c', 9)
    g.add_undirected_edge('a', 'f', 14)
    g.add_undirected_edge('b', 'c', 10)
    g.add_undirected_edge('b', 'd', 15)
    g.add_undirected_edge('c', 'd', 11)
    g.add_undirected_edge('c', 'f', 2)
    g.add_undirected_edge('d', 'e', 6)
    g.add_undirected_edge('e', 'f', 9)

    for v in g:
        for w in v.get_connections():
            print('( %s , %s, %3d)' % (v.val, w.val, v.get_weight(w)))

    for v in g:
        print('g.vert_dict[%s]=%s' % (v.get_id(), g.vertices[v.get_id()]))

    for vertex in g.dfs('a', set()):
        print(vertex)

    for vertex in g.bfs('a'):
        print(vertex)

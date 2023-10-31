"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/

Reference:
https://github.com/TheAlgorithms/Python/blob/master/data_structures/disjoint_set/disjoint_set.py
"""

from typing import Optional, List
from dataclasses import dataclass


@dataclass
class Node:
    """Dataclass represing node of the tree.
    """
    data: int
    rank: int
    parent: Optional['Node'] = None

    def __post_init__(self):
        self.parent = self


class DisjointSet:
    """DisjointSet Data Structure.
    """

    def __init__(self, sets: List[Node]) -> None:
        self.sets = sets

    def make_set(self, x: int) -> None:
        """Make x as a set.
        """
        # Cretae node with value=x, rank=0 and parent=None
        node = Node(x, 0)
        self.sets.append(node)
        return node

    def find_set(self, x: Node) -> Node:
        """Return the parent of x
        """
        if x != x.parent:
            x.parent = self.find_set(x.parent)
        return x.parent

    def union_set(self, x: Node, y: Node) -> None:
        """
        Union of two sets.
        set with bigger rank should be parent, so that the
        disjoint set tree will be more flat.
        """
        x, y = self.find_set(x), self.find_set(y)
        if x == y:
            return

        if x.rank == y.rank:
            x.parent = y
            y.rank += 1
        elif x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y

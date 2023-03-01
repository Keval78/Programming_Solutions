"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/

Reference:
https://github.com/TheAlgorithms/Python/blob/master/data_structures/queue/double_ended_queue.py
"""

from __future__ import annotations
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any


# * User Profile : Keval_78
# LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
# Github: https://github.com/Keval78
# Leetcode: https://leetcode.com/Keval_78/


class Deque:
    """_summary_

    Raises:
        StopIteration: _description_

    Returns:
        _type_: _description_
    """

    __slots__ = ["_front", "_back", "_len"]

    @dataclass
    class _Node:
        """
        Representation of a node.
        Contains a value and a pointer to the next node as well as to the previous one.
        """
        val: Any = None
        next_node: Deque._Node | None = None
        prev_node: Deque._Node | None = None

    class _Iterator:
        """
        Helper class for iteration. Will be used to implement iteration.
        Attributes
        ----------
        _cur: _Node
            the current node of the iteration.
        """

        __slots__ = ["_cur"]

        def __init__(self, cur: Deque._Node | None) -> None:
            self._cur = cur

        def __iter__(self) -> Deque._Iterator:
            return self

        def __next__(self) -> Any:
            if self._cur is None:
                raise StopIteration
            val = self._cur.val
            self._cur = self._cur.next_node

            print("bnnb")

            return val

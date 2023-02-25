"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/

Reference: https://github.com/TheAlgorithms/Python/blob/master/data_structures/queue/queue_on_list.py
"""


from __future__ import annotations
from typing import Generic, TypeVar

T = TypeVar("T")


class QueueLengthExceeded(BaseException):
    print("Queue Length Exceeded...")


class QueueLengthZero(BaseException):
    print("Queue Length Zero...")


class Queue(Generic[T]):
    def __init__(self, length: int = 10):
        self.queue: list[T] = []
        self.length = length

    def __bool__(self) -> bool:
        """Anything with length greater than 0 returns True."""
        return bool(self.queue)

    def __str__(self) -> str:
        return str(self.queue)

    def __contains__(self, item: T) -> bool:
        """Check if item is in queue"""
        return item in self.queue

    def put(self, item):
        if len(self.queue) >= self.length:
            raise QueueLengthExceeded
        self.queue.append(item)

    def get(self):
        if not self.queue:
            raise QueueLengthZero
        dequeued = self.queue[0]
        self.queue = self.queue[1:]
        return dequeued

    def size(self):
        return self.length

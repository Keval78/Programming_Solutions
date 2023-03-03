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


class PriorityQueue(Generic[T]):
    """PriorityQueue Data Structure
    """
    def __init__(self, size: int = 10, nitems: int = 0):
        self.__maxsize: int = size+1
        self.__queue: list[T] = []
        self.__nitems: int = nitems
    
    def __swim(self, pos: int):
        # Check if parent is smaller than child node
        while pos > 1 and self.__queue[pos//2] < self.__queue[pos]:
            temp = self.__queue[pos]
            self.__queue[pos] = self.__queue[pos//2]
            self.__queue[pos//2] = temp
            pos = pos//2
        # Promotion of child node will go on until it becomes smaller than the parent.

    def __sink(self, pos: int):
        # Check if node's position is that of parent node
        while 2*pos <= self.__nitems:
            # Jump to the positon of child node
            curr = 2*pos
            # Compare both the children for the greater one
            if curr < self.__nitems and self.__queue[curr] < self.__queue[curr+1]:
                curr+=1
            # If the parent node is greater, sink operation is complete. Break the loop
            if self.__queue[pos] >= self.__queue[curr]:
                break
            
            # If not exchange the value of parent with child
            temp = self.__queue[pos]
            self.__queue[pos] = self.__queue[curr]
            self.__queue[curr] = temp
            pos = curr # Exchange parent position to child position in the array

    def insert(self, value: T):
        # Print overflow message if the capacity is full
        if self.is_full():
            raise QueueLengthExceeded
        else:
            self.__queue[self.__nitems+1] = value
            self.__nitems += 1
            self.__swim(self.__nitems) # Swim up the element to its correct position

    def remove(self):
        if self.is_empty():
            raise QueueLengthZero
        else:
            # By defintion of our max-heap, value at queueArray[1] pos is the greatest
            max_ = self.__queue[1]
            # Swap max and last element
            temp = self.__queue[1]
            self.__queue[1] = self.__queue[self.__nitems]
            self.__queue[self.__nitems] = temp
            self.__queue[self.__nitems-1] = 0
            # Nullify the last element from the priority queue
            self.__nitems -= None
            # Sink the element in order
            self.__sink(1)
            return max_

    def peek(self):
        return self.__queue[1]
    
    def is_empty(self):
        return self.__nitems==0
    
    def is_full(self):
        return self.__nitems==self.__maxsize-1

    def getsize(self):
        return self.__nitems
    
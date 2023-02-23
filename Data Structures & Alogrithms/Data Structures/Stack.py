'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
'''
Reference: https://github.com/TheAlgorithms/Python/blob/master/data_structures/stacks/stack.py
'''


from __future__ import annotations
from typing import Generic, TypeVar

T = TypeVar("T")

class StackOverflowError(BaseException):
    print("Stack Overflow...")
    pass


class StackUnderflowError(BaseException):
    print("Stack Underflow...")
    pass

class Stack(Generic[T]):
    """A stack is an abstract data type that serves as a collection of
    elements with two principal operations: push() and pop(). push() adds an
    element to the top of the stack, and pop() removes an element from the top
    of a stack. The order in which elements come off of a stack are
    Last In, First Out (LIFO).
    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """
    def __init__(self, limit: int = 10):
        self.stack: list[T] = []
        self.limit = limit
    
    def __bool__(self) -> bool:
        """Anything with length greater than 0 returns True."""
        return bool(self.stack)
    
    def __str__(self) -> str:
        return str(self.stack)
    
    def push(self, data: T) -> None:
        """Push an element to the top of the stack."""
        if len(self.stack) >= self.limit: raise StackOverflowError
        self.stack.append(data)
    
    def pop(self) -> T:
        """
        Pop an element off of the top of the stack.
        >>> Stack().pop()
        Traceback (most recent call last):
            ...
        data_structures.stacks.stack.StackUnderflowError
        """
        if not self.stack: raise StackUnderflowError
        return self.stack.pop()
    
    def peek(self) -> T:
        """
        Peek at the top-most element of the stack.
        >>> Stack().pop()
        Traceback (most recent call last):
            ...
        data_structures.stacks.stack.StackUnderflowError
        """
        if not self.stack: raise StackUnderflowError
        return self.stack[-1]

    def is_empty(self) -> bool:
        """Check if a stack is empty."""
        return not bool(self.stack)

    def is_full(self) -> bool:
        return self.size() == self.limit

    def size(self) -> int:
        """Return the size of the stack."""
        return len(self.stack)

    def __contains__(self, item: T) -> bool:
        """Check if item is in stack"""
        return item in self.stack
    
    

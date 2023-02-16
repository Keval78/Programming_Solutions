'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
'''
Reference: https://github.com/TheAlgorithms/Python/blob/master/data_structures/linked_list/singly_linked_list.py
'''

from typing import Generic, TypeVar

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f"Node({self.data})"

class LinkedList(Generic[T]):
    def __init__(self):
        self.head = None
    
    def __iter__(self) -> T:
        node = self.head
        while node:
            yield node.data
            node = node.next
    
    def __len__(self) -> int:
        return len(tuple(iter(self)))
    
    def __repr__(self) -> str:
        return "->".join([str(item) for item in self])

    def __getitem__(self, index: int) -> T:
        if not 0 <= index < len(self):
            raise ValueError("list index out of range.")
        for i, node in enumerate(self):
            if i == index:
                return node
    
    def __setitem__(self, index: int, data: T) -> None:
        if not 0 <= index < len(self):
            raise ValueError("list index out of range.")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    def insert_head(self, data: T) -> None:
        return self.insert_nth(0, data)

    def insert_tail(self, data: T) -> None:
        return self.insert_nth(len(self), data)

    def insert_nth(self, index: int, data: T) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
    
    def print_list(self) -> None:
        print(self)
    
    def delete_head(self) -> T:
        return self.delete_nth()
    
    def delete_tail(self) -> T:
        return self.delete_nth(len(self))
    
    def delete_nth(self, index: int = 0) -> T:
        if not 0 <= index < len(self):
            raise IndexError("list index out of range.")
        delete_node = self.head
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
        return delete_node.data
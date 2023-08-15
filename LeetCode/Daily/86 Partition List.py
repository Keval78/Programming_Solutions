
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr and curr.val < x:
            prev = curr
            curr = curr.next
        if curr is None or curr.next is None:
            return head

        # print(prev, curr.val)
        while curr and curr.next:
            if curr.next.val >= x:
                curr = curr.next
            else:
                # move the node at prev
                node = curr.next
                # print(node.val)

                # Skip node...
                curr.next = curr.next.next

                # move the node at prev
                if prev:
                    node.next = prev.next
                    prev.next = node
                    prev = prev.next
                else:
                    node.next = head
                    head = prev = node

        return head

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            prev, curr = None, head
            while curr:
                curr.next, prev, curr = prev, curr, curr.next
            return prev

        head = reverse(head)
        l1 = l2 = head
        carry, curr, h1 = 0, l1, l1
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.val = carry % 10
            carry //= 10
            if curr.next is None and (l1 or l2 or carry):
                curr.next = ListNode(0)
            curr = curr.next

        return reverse(head)

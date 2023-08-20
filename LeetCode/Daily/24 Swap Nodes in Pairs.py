from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dummy = prev = ListNode(0, head)
        while curr and curr.next:
            # Swap nodes.
            prev.next = temp = curr.next
            curr.next = temp.next
            temp.next = curr

            # Go for next node
            prev = curr
            curr = curr.next

        return dummy.next

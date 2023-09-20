"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def printnode(k):
            while k:
                print(f"{k.val}->", end="")
                k = k.next
            print()

        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        dummy = ListNode(0, head)
        # prev, curr = None, head
        first, second = dummy, head

        prev = ans = None
        for j in range(0, n-k+1, k):
            curr = second  # pointing first node of the next group.
            for i in range(k):
                # Reverse k nodes
                if i == 0:
                    first.next = None
                second.next, first, second = first, second, second.next

            if j == 0:  # for first loop and our answer is kth node.
                ans = first

            if prev:
                prev.next = first
            dummy.next = second
            first = dummy
            prev = curr

        # change link of the last node.
        prev.next = second

        return ans

'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def main():
    class Solution:
        def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
                prev, curr = None, head
                while curr:
                    curr.next, prev, curr = prev, curr, curr.next
                return prev

            l1, l2 = reverse(l1), reverse(l2)
            carry, curr, h1 = 0, l1, l1
            while l1 or l2 or carry:
                # print(carry, l1.val if l1 else None, l2.val if l2 else None)
                if l1:
                    carry += l1.val
                    l1 = l1.next
                if l2:
                    carry += l2.val
                    l2 = l2.next
                # print(carry)
                curr.val = carry % 10
                carry //= 10
                if curr.next is None and (l1 or l2 or carry):
                    curr.next = ListNode(0)
                curr = curr.next
            return reverse(h1)


if __name__ == "__main__":
    main()

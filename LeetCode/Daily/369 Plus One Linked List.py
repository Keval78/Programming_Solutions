"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        start, curr = head, head
        # find the rightmost not-nine digit
        while curr is not None:
            if curr.val != 9: start = curr
            curr = curr.next
        
        # if start is 9 add 1 in the front.
        if start.val == 9:
            head, head.next = ListNode(1), head
        
        # increase all the following elements.
        while start is not None:
            start.val, start = (start.val+1)%10, start.next
        
        return head

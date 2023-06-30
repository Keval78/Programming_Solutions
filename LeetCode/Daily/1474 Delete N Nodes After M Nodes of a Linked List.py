"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

def main():
    class Solution:
        def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
            curr = head
            while curr:
                for i in range(m-1):
                    if curr.next is None: return head
                    curr = curr.next
                for i in range(n):
                    if curr.next is None: return head
                    curr.next = curr.next.next
                curr = curr.next
            return head


if __name__ == "__main__":
    main()

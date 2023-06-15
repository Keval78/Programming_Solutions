'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            head1, head2 = list1, list2
            merged = ListNode()
            prev = merged
            while head1 and head2:
                if head1.val <= head2.val:
                    prev.next, head1 = head1, head1.next
                else:
                    prev.next, head2 = head2, head2.next
                prev = prev.next
            
            if head1 is not None:
                prev.next = head1
            else:
                prev.next = head2
            
            return merged.next

    Solution().mergeTwoLists()


if __name__ == "__main__":
    main()




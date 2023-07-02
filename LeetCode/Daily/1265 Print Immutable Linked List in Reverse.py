"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

import math
class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        
        if head.getNext():
            self.printLinkedListInReverse(head.getNext())
        head.printValue()
    
    '''
    Time complexity: O(n).
    Space complexity: O(sqrt(n)).
    ''''''
    def printLinkedListInReverseRecursively(self, head: 'ImmutableListNode', size: int) -> None:
        if size > 0 and head is not None:
            self.printLinkedListInReverseRecursively(head.getNext(), size - 1)
            head.printValue()
    
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        curr, linked_list_size = head, 0
        while curr is not None:
            linked_list_size += 1
            curr = curr.getNext()
        
        curr, block_size = head, math.ceil(math.sqrt(linked_list_size))
        blocks = []
        for i in range(linked_list_size):
            if i % block_size == 0: blocks.append(curr)
            curr = curr.getNext()
        
        while blocks:
            self.printLinkedListInReverseRecursively(blocks.pop(), block_size)
    '''

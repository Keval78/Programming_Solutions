"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

def main():
    class Solution:
        def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
            node = Node(insertVal)
            if head is None:
                head, node.next = node, node
            else:
                curr = head
                while True:
                    if curr.val <= node.val <= curr.next.val or \
                        (curr.val > curr.next.val and (node.val>=curr.val or node.val<=curr.next.val)) or \
                        curr.next == head:
                        curr.next, node.next = node, curr.next
                        break
                    curr = curr.next
            return head


if __name__ == "__main__":
    main()

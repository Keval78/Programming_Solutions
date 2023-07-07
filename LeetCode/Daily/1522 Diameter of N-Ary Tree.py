'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

class Solution:
    def height(self, root: 'Node') -> int:
        if root is None: return 0
        largest, secondLargest = 0, 0
        for child in root.children:
            val = self.height(child)
            if val > largest:
                secondLargest = largest
                largest = val
            else:
                secondLargest = max(secondLargest, val)
        self.diameter = max(self.diameter, largest + secondLargest)
        return largest + 1

    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.diameter = 0
        self.height(root)
        return self.diameter
    
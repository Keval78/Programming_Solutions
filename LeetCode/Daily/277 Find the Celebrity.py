'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

class Solution:
    def is_celebrity(self, i, n):
        for j in range(n):
            if i==j: continue
            if knows(i,j) or not knows(j,i):
                return False
        return True
    
    def findCelebrity(self, n: int) -> int:
        celebrity_candidate = 0
        for i in range(1, n):
            if knows(celebrity_candidate, i):
                celebrity_candidate = i
        if self.is_celebrity(celebrity_candidate, n):
            return celebrity_candidate
        return -1
    
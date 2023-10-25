'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)

        n = len(processorTime)
        max_time = 0
        for i in range(n):
            curr = processorTime[i] + max([t for t in tasks[i*4:i*4+4]])
            max_time = max(curr, max_time)

        return max_time

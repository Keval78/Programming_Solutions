'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from collections import defaultdict

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        children = defaultdict(list)
        for i in range(len(ppid)):
            children[ppid[i]].append(pid[i])

        queue = collections.deque()
        queue.append(kill)
        result = []
        while queue:
            killed = queue.popleft()
            result.append(killed)
            if killed in children:
                queue.extend(children[killed])

        return result
    
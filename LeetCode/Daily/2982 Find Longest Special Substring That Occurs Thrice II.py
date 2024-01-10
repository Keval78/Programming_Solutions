'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def maximumLength(self, s: str) -> int:
        heaps = [[] for i in range(26)]
        n = len(s)

        length, prev = 0, s[0]
        for curr in s+'.':
            if curr == prev: 
                length+=1
            else: 
                # print(prev, length)
                idx = ord(prev) - 97
                if length > 0:
                    heappush(heaps[idx], length)
                    if len(heaps[idx]) > 3: heappop(heaps[idx])
                length = 1
            prev = curr
        # print(heaps)
        ans = 0
        for ch, heap in enumerate(heaps):
            curr_ans = 0
            heap.sort(reverse=True)
            if len(heap) > 0: curr_ans = max(curr_ans, heap[0]-2)
            if len(heap) > 1: curr_ans = max(curr_ans, min(heap[0]-1, heap[1]))
            if len(heap) > 2: curr_ans = max(curr_ans, min(heap[0], heap[1], heap[2]))
            # print(ch, curr_ans)
            ans = max(ans, curr_ans)
        return ans if ans!=0 else -1




s = "aaaa"
ans = Solution().maximumLength(s)
print(ans)



s = "abcdef"
ans = Solution().maximumLength(s)
print(ans)


s = "abcaba"
ans = Solution().maximumLength(s)
print(ans)


s = "abcabaabaacadaaaeaaaasaasaaa"
ans = Solution().maximumLength(s)
print(ans)

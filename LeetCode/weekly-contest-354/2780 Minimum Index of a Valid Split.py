
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        def findMajority(arr, n):
            '''Moore Voting Algorithms'''
            candidate = -1
            votes = 0
            for i in range(n):
                if (votes == 0):
                    candidate = arr[i]
                    votes = 1
                else:
                    if (arr[i] == candidate):
                        votes += 1
                    else:
                        votes -= 1
            count = 0
            for i in range(n):
                if (arr[i] == candidate):
                    count += 1
            return (candidate, count)
        n = len(nums)
        dom, count = findMajority(nums, n)
        ans, dom_count = -1, 0
        for i in range(n):
            dom_count += 1 if nums[i] == dom else 0
            if dom_count*2 > (i+1) and (count-dom_count)*2 > (n-i-1):
                ans = i
                break
        return ans

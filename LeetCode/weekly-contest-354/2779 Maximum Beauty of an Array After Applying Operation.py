from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        def overlap(v):
            ans = 0
            count = 0
            data = []
            for i in range(len(v)):
                data.append([v[i][0], 'x'])
                data.append([v[i][1], 'y'])
            data = sorted(data)
            for i in range(len(data)):
                if (data[i][1] == 'x'):
                    count += 1
                if (data[i][1] == 'y'):
                    count -= 1
                ans = max(ans, count)
            return ans

        v = [[i-k, i+k] for i in nums]
        return overlap(v)

from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(i, j, k) for i, j, k in zip(startTime, endTime, profit)]
        # print(jobs)
        jobs.sort(key=lambda x: x[0])
        # print(jobs)
        n = len(jobs)

        memo = [0 for i in range(len(jobs)+1)]

        def top_down_dp(jobs, idx):
            # Without memoization.
            if idx >= len(jobs):
                return 0

            if memo[idx] != 0:
                return memo[idx]

            next_job = len(jobs)
            l, r = idx, len(jobs)-1
            while l <= r:
                mid = (l+r)//2
                if jobs[mid][0] >= jobs[idx][1]:
                    r = mid-1
                else:
                    l = mid+1
            next_job = l

            res = max(
                # Skip the job at idx
                jobs[idx][2] + \
                top_down_dp(jobs, next_job), top_down_dp(jobs, idx+1)
            )
            memo[idx] = res
            return res

        ans = top_down_dp(jobs, 0)
        # print(ans)
        return ans

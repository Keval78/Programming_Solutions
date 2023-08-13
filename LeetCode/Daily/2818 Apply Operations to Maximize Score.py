from typing import List


class Solution:
    # def __init__(self):
    #     MAX = 10**5+1
    #     scores = [0 for i in range(MAX)]
    #     for i in range(2, MAX):
    #         if scores[i] != 0: continue
    #         for j in range(i, MAX, i):
    #             scores[j] += 1
    #     self.scores = scores

    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        MAX = max(nums)+1
        scores = [0 for i in range(MAX)]
        for i in range(2, MAX):
            if scores[i] != 0:
                continue
            for j in range(i, MAX, i):
                scores[j] += 1

        n = len(nums)
        primes = [scores[nums[i]] for i in range(n)]

        left, right = [-1]*n, [n]*n
        stack = []
        for i, num in enumerate(primes):
            while stack and primes[stack[-1]] < num:
                past = stack.pop()
                right[past] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        values = []
        for i, num in enumerate(nums):
            values.append((nums[i], (right[i]-i)*(i-left[i])))
        values.sort(key=lambda x: (-x[0], -x[1]))

        ans = 1
        for num, curr_op in values:
            if curr_op < k:
                ans = (ans * pow(num, curr_op, MOD)) % MOD
                k -= curr_op
            else:
                ans = (ans * pow(num, k, MOD)) % MOD
                break

        # print(ans)
        return ans

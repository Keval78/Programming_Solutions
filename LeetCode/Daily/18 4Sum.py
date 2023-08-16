from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        def twoSum(nums, target, num1, num2, start, end, res):
            i, j = start, end
            while i < j:
                curr = nums[i] + nums[j]
                if target < curr:
                    j -= 1
                elif target > curr:
                    i += 1
                else:
                    ans = (num1, num2, nums[i], nums[j])
                    res.add(ans)
                    # yield nums[i], nums[j]
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
        # -4 -1 -1 0 1 2
        res = set()
        n = len(nums)
        for i in range(n-3):
            for j in range(i+1, n-2):
                new_target = target-nums[i]-nums[j]
                twoSum(nums, new_target, nums[i], nums[j], j+1, n-1, res)
        return list(res)

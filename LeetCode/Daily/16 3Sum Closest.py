from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        def twoSum(nums, target, start, end, res):
            i, j = start, end
            curr = nums[i] + nums[j]
            while i < j:
                # print(i, j)
                curr = nums[i] + nums[j]
                if res[0] > abs(target-nums[i]-nums[j]):
                    res[0] = abs(target-nums[i]-nums[j])
                    res[1] = nums[start-1]+nums[i]+nums[j]
                # print(res)
                if target < curr:
                    j -= 1
                elif target >= curr:
                    i += 1
                else:
                    # yield nums[i], nums[j]
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    break
            return res
        # -4 -1 -1 0 1 2
        res = [float('inf'), float('inf')]
        n = len(nums)
        for i in range(n-2):
            if i == 0 or nums[i] != nums[i-1]:
                twoSum(nums, target-nums[i], i+1, n-1, res)
        return res[1]

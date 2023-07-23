class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        local_max = nums[-1]
        maxi = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] <= local_max:
                local_max += nums[i]
            else:
                local_max = nums[i]
            maxi = max(maxi, local_max)
        return maxi

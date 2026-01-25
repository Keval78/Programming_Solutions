'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from sortedcontainers import SortedSet

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        sum_with_idx = SortedSet((nums[i] + nums[i+1], i) for i in range(n-1))
        prev_next_idx = [[i-1, i+1] for i in range(n)]
        decreasing_pairs = sum(nums[i] > nums[i+1] for i in range(n-1))

        ops = 0
        while decreasing_pairs:
            pairsum, first = sum_with_idx.pop(0)
            second = prev_next_idx[first][1]  # Next index of first index

            first_prev = prev_next_idx[first][0]  # Prev index of first index 
            second_next = prev_next_idx[second][1]  # Next index of second index

            # Remove the merged decreasing pair
            if nums[first] > nums[second]:
                decreasing_pairs -= 1

            # ---------- Bad -> Good ----------
            if first_prev >= 0:
                if nums[first_prev] > nums[first] and nums[first_prev] <= pairsum:
                    decreasing_pairs -= 1
            if second_next < n:
                if nums[second] > nums[second_next] and pairsum <= nums[second_next]:
                    decreasing_pairs -= 1

            # ---------- Good -> Bad ----------
            if first_prev >= 0:
                if nums[first_prev] <= nums[first] and nums[first_prev] > pairsum:
                    decreasing_pairs += 1
            if second_next < n:
                if nums[second] <= nums[second_next] and pairsum > nums[second_next]:
                    decreasing_pairs += 1

            # ---------- Update sum_with_idx safely ----------
            if first_prev >= 0:
                sum_with_idx.remove((nums[first_prev] + nums[first], first_prev))
                sum_with_idx.add((nums[first_prev] + pairsum, first_prev))
            if second_next < n:
                sum_with_idx.remove((nums[second] + nums[second_next], second))
                sum_with_idx.add((pairsum + nums[second_next], first))

            # ---------- Relink neighbors ----------
            if second_next < n:
                prev_next_idx[second_next][0] = first
            prev_next_idx[first][1] = second_next

            # ---------- Merge ----------
            nums[first] = pairsum

            ops += 1
        return ops


nums = [5,2,3,1]
ans = Solution().minimumPairRemoval(nums)
print(ans)

nums = [1,2,2]
ans = Solution().minimumPairRemoval(nums)
print(ans)

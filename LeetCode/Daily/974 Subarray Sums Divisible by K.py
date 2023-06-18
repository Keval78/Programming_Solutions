"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from typing import List


def main():
    class Solution:
        def subarraysDivByK(self, nums: List[int], k: int) -> int:
            n_pairs = 0
            prefix_mod = 0

            mod_groups = [0]*k
            mod_groups[0] = 1

            for i, num in enumerate(nums):
                prefix_mod = ((prefix_mod+num) % k+k) % k
                n_pairs += mod_groups[prefix_mod]
                mod_groups[prefix_mod] += 1
            return n_pairs

    Solution().subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5)


if __name__ == "__main__":
    main()

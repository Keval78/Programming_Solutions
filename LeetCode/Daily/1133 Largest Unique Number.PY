"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from collections import defaultdict

def main():
    class Solution:
        def largestUniqueNumber(self, nums: List[int]) -> int:
            visit = [0]*1001
            for num in nums: visit[num] += 1
            for i in range(1000, -1, -1):
                if visit[i] == 1: return i
            return -1

    Solution().largestUniqueNumber()


if __name__ == "__main__":
    main()

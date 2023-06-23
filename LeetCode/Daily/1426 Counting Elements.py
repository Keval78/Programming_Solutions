"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from collections import defaultdict

def main():
    class Solution:
        def countElements(self, arr: List[int]) -> int:
            visit = [0]*1001
            for num in arr: visit[num] += 1
            total = 0
            for i in range(len(visit)-1):
                if visit[i+1] > 0: total += visit[i]
            return total

    Solution().countElements()


if __name__ == "__main__":
    main()

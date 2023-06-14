'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from collections import Counter

def main():
    class Solution:
        def maximumWealth(self, accounts: List[List[int]]) -> int:
            max_sum = 0
            for wealths in accounts:
                max_sum = max(max_sum, sum(wealths))
            return max_sum

    Solution().maximumWealth()


if __name__ == "__main__":
    main()

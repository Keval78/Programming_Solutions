"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List


def main():
    class Solution:
        def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
            intervals.sort()
            for i in range(1, len(intervals)):
                if intervals[i-1][1] > intervals[i][0]:
                    return False
            return True


if __name__ == "__main__":
    main()

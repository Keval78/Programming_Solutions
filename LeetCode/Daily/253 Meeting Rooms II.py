"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List

def main():
    class Solution:
        def minMeetingRooms(self, intervals: List[List[int]]) -> int:
            # Chronological Ordering
            used_rooms, n = 0, len(intervals)
            start_timings, end_timings = sorted([i[0] for i in intervals]), sorted([i[1] for i in intervals])
            start_pointer, end_pointer = 0, 0
            
            while start_pointer < n:
                if start_timings[start_pointer] >= end_timings[end_pointer]:
                    used_rooms -= 1
                    end_pointer += 1
                used_rooms += 1
                start_pointer += 1
            return used_rooms
                                    
    Solution().minMeetingRooms()


if __name__ == "__main__":
    main()

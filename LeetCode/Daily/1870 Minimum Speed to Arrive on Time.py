import math
class Solution:
    def issatisfy(self, dist: List[int], hour: float, speed: int) -> int:
        curr_hour = 0
        for d in dist[:-1]:
            curr_hour += math.ceil(d/speed)
            if curr_hour > hour:
                return False
        curr_hour += dist[-1]/speed
        if curr_hour > hour:
            return False
        else:
            return True

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if hour <= n-1: return -1
        low, high = 1, 10**8+1
        while (low <= high):
            mid = (low + high) // 2
            lr = self.issatisfy(dist, hour, mid)
            if not lr:
                low = mid + 1
            else:
                if (low == mid): break
                high = mid
        return mid
        
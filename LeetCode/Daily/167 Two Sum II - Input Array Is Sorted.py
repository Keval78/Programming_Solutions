from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        curr = numbers[i] + numbers[j]
        while i < j:
            curr = numbers[i] + numbers[j]
            if target < curr:
                j -= 1
            elif target > curr:
                i += 1
            else:
                return [i+1, j+1]

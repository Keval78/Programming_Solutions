"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from collections import OrderedDict
def main():
    class FirstUnique:
        def __init__(self, nums: List[int]):
            self._queue = OrderedDict()
            self._is_unique = {}
            for num in nums:
                self.add(num)

        def showFirstUnique(self) -> int:
            if self._queue:
                return next(iter(self._queue))
            return -1

        def add(self, value: int) -> None:
            if value not in self._is_unique:
                self._is_unique[value] = True
                self._queue[value] = None
            elif self._is_unique[value]:
                self._is_unique[value] = False
                self._queue.pop(value)


if __name__ == "__main__":
    main()

"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from collections import deque

def main():
    class MovingAverage:
        def __init__(self, size: int):
            self.que = deque()
            self.size = size 

        def next(self, val: int) -> float:
            self.que.append(val)
            if len(self.que)>self.size: self.que.popleft()
            return sum(self.que)/len(self.que)


if __name__ == "__main__":
    main()

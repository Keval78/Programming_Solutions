'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def judgeCircle(self, moves: str) -> bool:
            ud, lr = 0, 0
            for move in moves:
                match move:
                    case "U": ud += 1
                    case "D": ud -= 1
                    case "L": lr += 1
                    case "R": lr -= 1
            return ud|lr == 0
    Solution().judgeCircle()


if __name__ == "__main__":
    main()

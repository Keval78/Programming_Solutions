'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from collections import Counter

def main():
    class Solution:
        def isRobotBounded(self, instructions: str) -> bool:
            ud, lr = 0, 0
            dire = "U"
            instructions = 4*instructions
            for inst in instructions:
                match inst:
                    case "G":
                        match dire:
                            case "U": ud += 1
                            case "D": ud -= 1
                            case "L": lr -= 1
                            case _: lr += 1
                    case "L":
                        match dire:
                            case "U": dire = "L"
                            case "D": dire = "R"
                            case "L": dire = "D"
                            case _: dire = "U"
                    case "R":
                        match dire:
                            case "U": dire = "R"
                            case "D": dire = "L"
                            case "L": dire = "U"
                            case _: dire = "D"
            return ud|lr == 0

    Solution().isRobotBounded()


if __name__ == "__main__":
    main()

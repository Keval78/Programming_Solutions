'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def calPoints(self, operations: List[str]) -> int:
            stack = []
            for op in operations:
                match(op):
                    case "+": stack.append(stack[-1]+stack[-2])
                    case "D": stack.append(stack[-1]*2)
                    case "C": stack.pop()
                    case _: stack.append(int(op))
            return sum(stack)
    Solution().calPoints()


if __name__ == "__main__":
    main()

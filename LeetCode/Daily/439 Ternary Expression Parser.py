'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

#import collections
from collections import deque

def main():
    class Solution:
        def parseTernary(self, expression: str) -> str:
            stack = deque()
            for ch in reversed(expression):
                if len(stack)>0 and stack[-1] == '?':
                    op = ch
                    ques = stack.pop()
                    if_val = stack.pop()
                    coln = stack.pop()
                    els_val = stack.pop()

                    output = if_val if op == "T" else els_val
                    stack.append(output)
                else:
                    stack.append(ch)
            return stack[0]

    
    Solution().parseTernary()


if __name__ == "__main__":
    main()

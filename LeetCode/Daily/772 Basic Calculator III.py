"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from collections import deque

def main():
    class Solution:
        def calculate(self, s: str) -> int:
            stack = deque()
            def push(op, num):
                if op == "+": stack.append(num)
                elif op == "-": stack.append(-num)
                elif op == "*": stack.append(stack.pop()*num)
                elif op == "/": stack.append(int(stack.pop()/num))
        
            op, num = "+", 0
            for ch in s:
                if ch.isdigit():
                    num = num*10 + int(ch)
                elif ch == "(":
                    stack.append(op)
                    op, num = "+", 0
                elif ch in ["+", "-", "*", "/", ")"]:
                    push(op, num)
                    if ch == ")":
                        num = 0
                        while isinstance(stack[-1], int): num += stack.pop()
                        push(stack.pop(), num)
                    op, num = ch, 0
            push(op, num)
            
            return sum(stack)

    Solution().calculate()


if __name__ == "__main__":
    main()

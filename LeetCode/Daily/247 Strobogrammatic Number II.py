'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = []
        stbg = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6', }

        def rec_create_half_num(stack, res, stbg):
            if len(stack) == n//2:
                if n % 2:
                    for key in ['0', '1', '8']:
                        res.append(
                            "".join(stack + [key] + [stbg[i] for i in stack[::-1]]))
                else:
                    res.append("".join(stack + [stbg[i] for i in stack[::-1]]))
                return

            for key in stbg:
                if len(stack) == 0 and key == "0":
                    continue
                stack.append(key)
                rec_create_half_num(stack, res, stbg)
                stack.pop()

        rec_create_half_num([], res, stbg)
        return res

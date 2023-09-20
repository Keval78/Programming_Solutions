"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        rtoi = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
                (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
                (5, "V"), (4, "IV"), (1, "I")]

        roman = []
        for value, symbol in rtoi:
            if num == 0:
                break
            count, num = divmod(num, value)
            roman.append(symbol * count)
        return "".join(roman)

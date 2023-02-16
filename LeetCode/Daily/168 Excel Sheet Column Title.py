'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def convertToTitle(self, columnNumber: int) -> str:
            column = ""
            while columnNumber > 0:
                column = chr(columnNumber%26 + 64) + column
                columnNumber -= columnNumber%26 if columnNumber%26!=0 else 26
                columnNumber = columnNumber//26
            return column.replace("@","Z")
            
    Solution().convertToTitle(columnNumber = 701)


if __name__ == "__main__":
    main()

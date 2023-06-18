'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def toLowerCase(self, s: str) -> str:
            is_upper = lambda x : 'A' <= x <= 'Z'
            to_lower = lambda x : chr(ord(x) | 32)

            return ''.join([to_lower(x) if is_upper(x) else x for x in s])
    
    Solution().toLowerCase()


if __name__ == "__main__":
    main()

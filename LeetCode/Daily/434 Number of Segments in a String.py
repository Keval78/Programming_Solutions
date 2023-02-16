'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def countSegments(self, s: str) -> int:
            cnt, checker  = 0, False
            for i in s:
                if i == ' ' and checker: 
                    checker = False
                    cnt+=1
                if i != ' ': checker = True
            return  cnt+1 if checker else cnt
            
    Solution().captureForts(forts = [1,0,0,-1,0,0,0,0,1])


if __name__ == "__main__":
    main()

'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
            diff, prev = None, None
            for i in sorted(arr):
                if prev != None:
                    if diff==None: diff = prev-i
                    print(diff, prev, i)
                    if prev-i != diff:
                        return False
                prev = i
            return True
    
    Solution().canMakeArithmeticProgression()


if __name__ == "__main__":
    main()

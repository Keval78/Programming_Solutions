'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def arraySign(self, nums: List[int]) -> int:
            neg_count = 0
            for i in nums:
                if i==0: return 0
                if i<0: neg_count += 1
            return 1 if neg_count%2==0 else -1
    
    Solution().arraySign()


if __name__ == "__main__":
    main()

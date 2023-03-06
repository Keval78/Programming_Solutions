"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

def main():
    class Solution:
        curr = 0
        def numPairsDivisibleBy60(self, time: List[int]) -> int:
            mod = [0]*60
            for t in time:
                mod[t%60] += 1
            i,j = 0, len(mod)//2
            pairs = (mod[i]*(mod[i]-1) + mod[j]*(mod[j]-1))//2
            for i in range(1, len(mod)//2):
                pairs += mod[i]*mod[len(mod)-i]
            return pairs
            
    Solution().numPairsDivisibleBy60()


if __name__ == "__main__":
    main()

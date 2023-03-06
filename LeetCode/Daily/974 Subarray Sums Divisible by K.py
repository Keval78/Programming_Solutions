"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

def main():
    class Solution:
        # NEED TO WORK
        def subarraysDivByK(self, nums: List[int], k: int) -> int:
            n_pairs = 0
        
            prefix = nums.copy()
            prefix[1:] = [prefix[i-1] + nums[i] for i in range(1, len(nums))]
            print(prefix)

            for i in range(len(nums)-1):
                for j in range(i, len(nums)):
                    if prefix[i]%k==prefix[j]%k:
                        n_pairs+=1

            return n_pairs
            
    Solution().subarraysDivByK()


if __name__ == "__main__":
    main()

'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        # Solution 
        # Step1: write Binary search to find num whose sum val <= K
        # Step2: Write a function which find sum in Log(num) Time complexity.
        
        bits = 64
        def price_sum(num, sums):
            # Recursive function to calculate price sum.
            if num == 0: return
            
            n, bits = 1, 0
            while n <= num:
                n, bits = n*2, bits+1
            n, bits = n//2, bits-1
            
            for i in range(bits):
                sums[-i-1] += (n//2)
            sums[-bits-1] += num - n + 1
            
            price_sum(num - n, sums)

        ans = 0
        l, r = 1, 10**16
        while l < r:
            mid = (l+r)//2
            
            sums = [0]*bits
            price_sum(mid, sums)
            curr_val = sum([sums[-i] for i in range(1, bits+1) if i%x==0])

            if curr_val <= k:
                ans = mid
                l = mid + 1
            else:
                r = mid

        return ans


k = 9
x = 1
ans = Solution().findMaximumNumber(k, x)
print(ans)

k = 30
x = 1
ans = Solution().findMaximumNumber(k, x)
print(ans)

k = 7
x = 2
ans = Solution().findMaximumNumber(k, x)
print(ans)

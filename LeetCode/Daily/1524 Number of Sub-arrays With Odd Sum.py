class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9+7
        odd, even = 0, 1
        total = 0
        ans = 0
        for num in arr:
            total += num
            if total%2: 
                odd += 1
                ans += even
            else: 
                even+=1
                ans += odd
            ans %= MOD
        #print(ans)
        return ans
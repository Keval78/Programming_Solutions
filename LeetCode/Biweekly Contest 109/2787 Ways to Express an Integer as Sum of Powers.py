class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
        power = x
        dp = [[-1 for i in range(n+3)] for j in range(n+3)]

        def numberOfWaysHelper(currsum, base):
            if currsum == n:
                return 1
            if n < pow(base, power) or currsum > n:
                return 0
            if dp[currsum][base] != -1:
                return dp[currsum][base]
            result = pow(base, power)
            take = numberOfWaysHelper(currsum+result, base+1)
            nontake = numberOfWaysHelper(currsum, base+1)
            dp[currsum][base] = (take+nontake) % mod
            return dp[currsum][base]
        return numberOfWaysHelper(0, 1)

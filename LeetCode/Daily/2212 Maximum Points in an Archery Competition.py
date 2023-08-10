class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        def dp(mask, remaining, aliceArrows):
            # print(mask, remaining)
            if memo[mask] > 0: return memo[mask]
            if remaining <= 0: return 0
            for i in range(1, 12):
                # print(i, mask, remaining, remaining>aliceArrows[i])
                if mask & (1<<i) == 0 and remaining>aliceArrows[i]:
                    memo[mask|(1<<i)] = dp(mask|(1<<i), remaining-aliceArrows[i]-1, aliceArrows) + i
                    # print(memo[mask|(1<<i)])
            return memo[mask]
        memo = [0 for i in range(2**12)]
        dp(0, numArrows, aliceArrows)
        
        ind, maxi = max(enumerate(memo), key=lambda x:x[1])
        bobarrowbin = bin(ind)[:1:-1]
        n = len(bobarrowbin)
        
        bobArrows = [0]*12
        for i in range(12):
            if i<n and bobarrowbin[i]=="1":
                bobArrows[i] = aliceArrows[i]+1
        bobArrows[0] = numArrows - sum(bobArrows)
        return bobArrows

        

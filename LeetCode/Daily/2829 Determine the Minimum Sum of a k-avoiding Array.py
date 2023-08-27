class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        if k == 1:
            return ((n)*(n+1))//2
        else:
            ans = 0
            for i in range(1, min(n+1, k//2+1)):
                ans += i
            # print(k, n - k//2)
            for i in range(0, n - k//2):
                # print(i+k)
                ans += i+k
            return ans

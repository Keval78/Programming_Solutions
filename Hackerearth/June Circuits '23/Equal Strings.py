'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''


def ii(): return int(input())
def si(): return input()
def mi(ss=" "): return map(int, input().strip().split(ss))
def msi(ss=" "): return map(str, input().strip().split(ss))
def li(ss=" "): return list(mi(ss))


for _ in range(ii()):
    n, x = mi()
    # s, t = msi()
    s, t = si(), si()
    mismatches = []
    for i in range(n):
        if s[i] != t[i]:
            mismatches.append(i)

    if len(mismatches) % 2:
        print("-1")
    else:
        m = len(mismatches)
        dp = [[-1 for j in range(n+1)] for i in range(n+1)]
        # print(m, n)
        # base case
        for j in range(n):
            dp[m][j] = 0 if j == 0 else float('inf')
        for i in range(m-1, -1, -1):
            for j in range(m, -1, -1):
                dp[i][j] = dp[i+1][j]+x
                if i+1 < m:
                    dp[i][j] = dp[i][j] = min(
                        dp[i][j], dp[i+2][j] + min(x, mismatches[i+1]-mismatches[i]))
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i+1][j-1])
        for i in range(n):
            print(dp[i])
        # print(dp[0][0])

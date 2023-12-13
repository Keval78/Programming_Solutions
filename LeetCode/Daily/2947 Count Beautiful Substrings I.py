'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        cntv, cntc = [0]*(n+1), [0]*(n+1)
        # print(s)
        for i in range(1, n+1):
            cntv[i] += cntv[i-1]
            cntc[i] += cntc[i-1]
            if s[i-1] in vowels:
                cntv[i] += 1 
            else:
                cntc[i] += 1 
        ans = 0
        for i in range(1, n+1):
            for j in range(i, n+1):
                c, v = cntc[j]-cntc[i-1], cntv[j]-cntv[i-1]
                if c==v and (c*v)%k==0:
                    ans+=1
        return ans



s = "baeyh"
k = 2
ans = Solution().beautifulSubstrings(s, k)
print(ans)


s = "abba"
k = 1
ans = Solution().beautifulSubstrings(s, k)
print(ans)

s = "bcdf"
k = 1
ans = Solution().beautifulSubstrings(s, k)
print(ans)

s = "ba"*20
k = 2
ans = Solution().beautifulSubstrings(s, k)
print(ans)



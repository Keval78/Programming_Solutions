'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from collections import Counter

def main():
    class Solution:
        def repeatedSubstringPattern(self, s: str) -> bool:
            # for i in range(1,len(s)):
            #     if len(s)%i==0:
            #         for j in range(len(s)):
            #             if s[j] != s[j%i]:
            #                 break
            #             if s[j] == s[j%i] and j==len(s)-1:
            #                 return True
            # return False
            #solve using KMP's LPS
            lps = [0]*len(s)
            prevLps, i = 0, 1
            while i < len(s):
                if s[prevLps] == s[i]:
                    lps[i] = prevLps+1
                    prevLps += 1
                    i += 1
                else:
                    if prevLps == 0:
                        lps[i]=0
                        i+=1
                    else:
                        prevLps = lps[prevLps-1]
            
            last = lps[-1]
            if last!=0 and last%(len(s)-last)==0:
                return True
            return False
    
    Solution().repeatedSubstringPattern("abcabc")


if __name__ == "__main__":
    main()

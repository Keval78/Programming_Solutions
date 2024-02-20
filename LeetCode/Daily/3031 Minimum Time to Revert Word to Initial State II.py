'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)

        def get_lps_array(pattern: str) -> list[int]:
            """
            Longest Prefix Suffix Array
            Calculates the new index we should go to if we fail a comparison
            """
            lps, prevLps, i = [0], 0, 1
            while i < len(pattern):
                if pattern[prevLps] == pattern[i]:
                    prevLps += 1
                elif prevLps > 0:
                    prevLps = lps[prevLps-1]
                    continue
                i += 1
                lps.append(prevLps)
            return lps

        lps = get_lps_array(word)
        print(lps)
        
        idx = lps[-1]
        while idx>0 and (n-idx)%k != 0:
            idx = lps[idx-1]
        ans = (n-idx)//k + ((n-idx)%k!=0)

        return ans

    
    def minimumTimeToInitialState2(self, word: str, k: int) -> int:
        """
        Substring algoruthm with hashing.
        """
        n = len(word)
        p, MOD = 31, 10**9+7
        p_pow, pref_hash = [1]*(n+1), [0]*(n+1)
        
        for i in range(1, n+1):
            p_pow[i] = (p_pow[i-1]*p)%MOD
            pref_hash[i] = pref_hash[i-1] + ((ord(word[i-1])-ord('a')+1)*p_pow[i])%MOD
        
        ans = n//k + (n%k!=0)
        for j in range(k, n, k):
            # remaining => n-j characters
            hash_front = (pref_hash[n-j] * p_pow[j])%MOD
            hash_back = (pref_hash[n] - pref_hash[j] + MOD)%MOD
            
            if hash_front == hash_back and word[j:] == word[:n-j]:
                ans = j//k
                break

        return ans

word = "abacaba"
k = 3
ans = Solution().minimumTimeToInitialState(word, k)
print(ans)

word = "abacaba"
k = 4
ans = Solution().minimumTimeToInitialState(word, k)
print(ans)

word = "abcbabcd"
k = 2
ans = Solution().minimumTimeToInitialState(word, k)
print(ans)

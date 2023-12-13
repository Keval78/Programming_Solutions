'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

import math
from collections import defaultdict

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        pref = [0]*(n+1)
        cnt = defaultdict(int)

        # TODO: Solution: Approach 1
        # Take vowel = 1 and consonant = -1
        # Generate Prefix sum and its count to find substring where vowels==consonants
        
        #*  (L^2/4)%K  ==  0
        #*  L = (j-i)
        
        #*  Skip division of 4
        #*  L^2%K  ==  0
        
        #*  K  =  P1^K1 * P2^K2 * P3^K3 ....
        #*  L  =  P1^L1 * P2^L2 * P3^L3 ....
        
        #*  2*Li   >=  Ki
        #*  Li     >=  math.ciel(Ki//2) = K'
        
        #*  L % K' == 0
        #*  (j-i) % K' == 0
        #*  j%K' == i%K'
        
        #* for P == 2  =>  math.ciel(Ki//2) + 1
        #* for other P  =>  math.ciel(Ki//2)
        
        # Let's find the primes till all the K.
        
        k_dash = 1
        for i in range(2, k+1):
            i_cnt = 0
            while k%i == 0:
                i_cnt += 1
                k //= i
            
            if i == 2:
                np = math.ceil(i_cnt/2) + 1
                k_dash *= i ** np
            else:
                np = math.ceil(i_cnt/2)
                k_dash *= i ** np
        
        # print(k_dash)
        
        cnt[(0, 0)] = 1
        ans = 0
        for i in range(1, n+1):
            pref[i] += pref[i-1] + (1 if s[i-1] in vowels else -1)
            
            # print((pref[i], i%k_dash))
            ans += cnt[(pref[i], i%k_dash)]
            cnt[(pref[i], i%k_dash)] += 1
        
        # print(pref)
        # print(cnt)

        return ans
    
    
    def beautifulSubstrings2(self, s: str, k: int) -> int:
        n = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        pref = [0]*(n+1)

        # TODO: Solution: Approach 2
        # https://www.youtube.com/watch?v=Th4jtNqzyEc
        # Take vowel = 1 and consonant = -1
        # Generate Prefix sum and its count to find substring where vowels==consonants
        
        vowel = 0
        consonant = 0
        result = 0
        
        ans = 0
        cnt = {}  # key = (v-c), value = dictionary (vowel count in the past -> count)
        cnt[0] = {0: 1}
        for i in range(1, n+1):
            if s[i-1] in vowels:
                vowel += 1 
            else:
                consonant += 1
            
            pSum = vowel - consonant
            for pastVowelCount, count in cnt.get(pSum, {}).items():
                # current substring vowel count = vowel - pastVowelCount
                if (vowel % k - pastVowelCount) * (vowel % k - pastVowelCount) % k == 0:
                    result += count
            
            cnt.setdefault(pSum, {}).setdefault(vowel % k, 0)
            cnt[pSum][vowel % k] += 1
        
        print(result)

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



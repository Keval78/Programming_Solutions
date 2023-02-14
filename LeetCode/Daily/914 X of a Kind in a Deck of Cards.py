'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from collections import Counter

def main():
    class Solution:
        def hasGroupsSizeX(self, deck: List[int]) -> bool:
            deck_c = Counter(deck)

            m = min(list(deck_c.values()))
            for j in range(2,m+1):
                for i in deck_c:
                    if deck_c[i]%j != 0:
                        break
                else:
                    return True
            return False
        
        '''
        def gcd(self, a, b):
                if a % b == 0: return b
                else: return self.gcd(b, a % b)
                
        def hasGroupsSizeX(self, deck: List[int]) -> bool:
            
            if len(deck) <= 1: return False
            
            counter = Counter(deck)
            if len(counter) == 1: return True
            
            g = counter[deck[0]]
            for v in counter.values():
                g = self.gcd(g, v)
                if g == 1: return False   
            return True
        '''

    Solution().hasGroupsSizeX(deck = [1,2,3,4,4,3,2,1])


if __name__ == "__main__":
    main()

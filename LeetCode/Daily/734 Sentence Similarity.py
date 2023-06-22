"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from collections import defaultdict

def main():
    class Solution:
        def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
            if len(sentence1)!=len(sentence2): return False
            pairs = defaultdict(set)
            for pair in similarPairs:
                pairs[pair[0]].add(pair[1])
                pairs[pair[1]].add(pair[0])
            for s1, s2 in zip(sentence1, sentence2):
                if s1!=s2 and s2 not in pairs[s1]: return False
            return True


    Solution().areSentencesSimilar()


if __name__ == "__main__":
    main()

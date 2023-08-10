class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        visit = {}
        cnt = 0
        for val in freq.values():
            while val>0 and val in visit:
                val-=1
                cnt += 1
            visit[val] = True
                
        return cnt
        
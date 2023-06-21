"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

def main():
    class Solution:
        def shortestWay(self, source: str, target: str) -> int:
            n, m = len(source), len(target)
            
            present = [False]*26
            for i in range(n):
                present[ord(source[i])-ord('a')] = True
            for i in range(m):
                if not present[ord(target[i])-ord('a')]:
                    return -1
            
            i, j, count = 0, 0, 0
            while(j<m):
                if source[i%n] == target[j]: i, j = i+1, j+1
                else: i+=1
                if i%n==0: count+=1
            if i%n!=0: count+=1
            return count
            
    Solution().shortestWay()


if __name__ == "__main__":
    main()

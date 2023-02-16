'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def captureForts(self, forts: List[int]) -> int:
            ans, cnt = 0, 0
            for i in range(len(forts)):
                if forts[i] == 0: cnt += 1
                else:
                    if i-cnt>0 and (forts[i]==1 and forts[i-cnt-1]==-1) or (forts[i]==-1 and forts[i-cnt-1]==1):
                        ans = max(ans, cnt)
                    cnt = 0
            return ans
            
    Solution().captureForts(forts = [1,0,0,-1,0,0,0,0,1])


if __name__ == "__main__":
    main()

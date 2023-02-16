'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def checkIfExist(self, arr: List[int]) -> bool:
            double = collections.defaultdict()
            for i in arr:
                if double.get(i*2,0) or double.get(i/2,0): return True
                double[i] = True
            return False
            
    Solution().checkIfExist(arr = [10,2,5,3])


if __name__ == "__main__":
    main()

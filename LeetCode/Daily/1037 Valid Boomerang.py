'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def isBoomerang(self, points: List[List[int]]) -> bool:
            x1, y1, x2, y2, x3, y3 = points[0] + points[1] + points[2]
            area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2
            return area != 0
            
    Solution().isBoomerang(points = [[1,1],[2,3],[3,2]])


if __name__ == "__main__":
    main()

'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
            if coordinates[1][0] != coordinates[0][0]:
                m = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
                c = coordinates[0][1] - (m*coordinates[0][0])
                for coordi in coordinates:
                    if coordi[1] != (m*coordi[0])+c:
                        return False
            else:
                for coordi in coordinates:
                    if coordi[0] != coordinates[1][0]:
                        return False
            return True
            
    Solution().checkStraightLine()


if __name__ == "__main__":
    main()




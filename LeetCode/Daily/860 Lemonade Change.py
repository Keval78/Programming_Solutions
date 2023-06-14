'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def lemonadeChange(self, bills: List[int]) -> bool:
            changes = [0,0]
            for bill in bills:
                match bill:
                    case 5: changes[0]+=1
                    case 10: 
                        changes[0] -= 1
                        changes[1] += 1
                    case _:
                        if changes[1]>0 and changes[0]>0:
                            changes[0] -= 1
                            changes[1] -= 1
                        else:
                            changes[0] -= 3
                if changes[0]<0 or changes[1]<0:
                    return False
            return True
            
    Solution().lemonadeChange()


if __name__ == "__main__":
    main()




'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def average(self, salary: List[int]) -> float:
            mini, maxi = salary[0], salary[0]
            for sal in salary:
                if sal < mini:
                    mini = sal
                if sal > maxi:
                    maxi = sal
            total_sal = 0
            total = 0   
            for sal in salary:
                if sal != mini and sal != maxi:
                    total_sal += sal
                    total += 1
            return total_sal/total
            
    Solution().average()


if __name__ == "__main__":
    main()




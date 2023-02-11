'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def buddyStrings(self, s: str, goal: str) -> bool:
            # check same length
            if len(s) != len(goal): return False
            
            # if strings are equal - check if there is a double to swap
            if s == goal:
                return True if len(s) - len(set(s)) >= 1 else False
            
            # count differences between strings
            diff = []
            for i in range(len(s)):
                if s[i] != goal[i]:
                    diff.append(i)
                    if len(diff) > 2: return False
                    
            # not exactly two differences
            if len(diff) != 2: return False
            
            # check if can be swapped
            if s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]:
                return True
            
            return False
            
    Solution().buddyStrings("ab", "ba")


if __name__ == "__main__":
    main()

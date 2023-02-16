'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def numDifferentIntegers(self, word: str) -> int:
            nums = set()
            i = 0
            while i < len(word):
                if word[i].isdigit():
                    num = ""
                    while i < len(word) and word[i].isdigit():
                        num += word[i]
                        i += 1
                    nums.add(int(num))
                i += 1
            return len(nums)
            
    Solution().numDifferentIntegers(word = "leet1234code234")


if __name__ == "__main__":
    main()

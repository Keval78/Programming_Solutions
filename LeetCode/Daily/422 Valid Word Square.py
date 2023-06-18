'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def validWordSquare(self, words: List[str]) -> bool:
            for i in range(len(words)):
                for j in range(len(words[i])):
                    if j>=len(words) or i>=len(words[j]) or words[i][j] != words[j][i]:
                        return False
            return True

    Solution().invertTree()


if __name__ == "__main__":
    main()




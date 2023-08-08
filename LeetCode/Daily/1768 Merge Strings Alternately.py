'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''


def main():
    class Solution:
        def mergeAlternately(self, word1: str, word2: str) -> str:
            merged = ""
            for i in range(min(len(word1), len(word2))):
                merged += f"{word1[i]}{word2[i]}"

            for j in range(i+1, len(word1)):
                merged += f"{word1[j]}"
            for j in range(i+1, len(word2)):
                merged += f"{word2[j]}"

            # for i,j in zip_longest(word1,word2, fillvalue=''):
            #     merged += f"{i}{j}"

            return merged

    # Solution().mergeAlternately()


if __name__ == "__main__":
    main()

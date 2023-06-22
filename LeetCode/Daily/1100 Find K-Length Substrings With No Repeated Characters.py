"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

def main():
    class Solution:
        def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
            if k > 26: return 0
            answer = 0
            left = right = 0
            freq = [0] * 26

            get_val = lambda ch: ord(ch) - ord('a')
            while right < len(s):
                freq[get_val(s[right])] += 1
                while freq[get_val(s[right])] > 1:
                    freq[get_val(s[left])] -= 1
                    left += 1
                if right - left + 1 == k:
                    answer += 1
                    freq[get_val(s[left])] -= 1
                    left += 1
                right += 1
            return answer


    Solution().numKLenSubstrNoRepeats()


if __name__ == "__main__":
    main()

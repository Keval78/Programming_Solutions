"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List


class Solution:
    def convertlisttostr(self, curr_list, maxWidth):
        currlen = 0
        for word in curr_list:
            currlen += len(word)

        need = maxWidth - currlen
        # print(need, curr_list)
        if len(curr_list) == 1:
            line = curr_list[0] + " "*(need)
        else:
            line = ""
            spaces, mod = divmod(need, len(curr_list)-1)
            # print(spaces, mod, need, len(curr_list)-1)
            for w in curr_list:
                if mod > 0:
                    line += w + " "*(spaces+1)
                else:
                    line += w + " "*(spaces)
                mod -= 1
            line = line.strip()
        return line

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []

        curr = 0
        curr_list = []
        for word in words:
            curr += len(word)
            if curr > maxWidth:
                line = self.convertlisttostr(curr_list, maxWidth)
                res.append(line)
                curr_list = [word]
                curr = len(word)
            else:
                curr_list.append(word)
            curr += 1

        if curr_list:
            curr_list = [" ".join(curr_list)]
            line = self.convertlisttostr(curr_list, maxWidth)
            res.append(line)

        return res

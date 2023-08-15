class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = ""
        n = len(s)
        row_inc = 2*numRows-2
        spaces = numRows-2
        for j in range(numRows):
            for i in range(j, n, row_inc):
                ans += s[i]
                if j != 0 and j != numRows-1:
                    k = (numRows-j-1)*2
                    if i+k < n:
                        ans += s[i+k]
        return ans

'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''


def ii(): return int(input())
def si(): return input()
def mi(ss=" "): return map(int, input().strip().split(ss))
def msi(ss=" "): return map(str, input().strip().split(ss))
def li(ss=" "): return list(mi(ss))


for _ in range(ii()):
    n, arr = ii(), li()
    mas = float('inf')

    def subset(ind, a, b, n):
        global mas
        if ind == n:
            mas = min(mas, abs(a**2-b**2))
        else:
            subset(ind+1, a+arr[ind], b, n)
            subset(ind+1, a, b+arr[ind], n)

    subset(0, 0, 0, n)
    print(mas)

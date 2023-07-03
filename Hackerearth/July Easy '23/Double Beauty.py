'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
import heapq


def ii(): return int(input())
def si(): return input()
def mi(ss=" "): return map(int, input().strip().split(ss))
def msi(ss=" "): return map(str, input().strip().split(ss))
def li(ss=" "): return list(mi(ss))


for _ in range(ii()):
    n, k = mi()
    arr = li()
    heapq.heapify(arr)
    max_sum = 2 * sum(heapq.nlargest(k, arr))
    print(max_sum)

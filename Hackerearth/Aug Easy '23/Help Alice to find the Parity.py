import sys

def si(): return sys.stdin.readline().strip()
def mi(ss=" "): return map(int, si().split(ss))

L, R = mi()
if L%2==0:
    if ((R-L+1)//2)%2==0:
        print("even")
    else:
        print("odd")
else:
    if ((R-L)//2)%2==0:
        print("odd")
    else:
        print("even")
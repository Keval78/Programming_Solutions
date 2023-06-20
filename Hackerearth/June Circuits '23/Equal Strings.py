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
    def bit_count(x): return bin(x).count("1")

    count_zero = 0
    ans = 0
    parity_flag = "EVEN"
    prev_parity = (0, 0)
    for i in range(n):
        if bit_count(arr[i]) % 2 == 0:  # Number has even number of set bits.
            count_zero += count_zero + 1
        else:
            ans += count_zero + 1
            if ans != 0:
                ans += count_zero
            count_zero = 0

            if parity_flag == "EVEN":
                prev_parity[1] + 1
    print(ans)

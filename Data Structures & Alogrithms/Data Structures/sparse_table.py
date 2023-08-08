MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1


class SparseTable:
    def __init__(self, arr, func, init):
        self.func = func
        self.init = init
        n = len(arr)
        k = n.bit_length() + 1

        bin_log = [0 for i in range(MAX)]
        bin_log[1] = 0
        for i in range(2, n+1):
            bin_log[i] = bin_log[i//2]+1
        self.bin_log = bin_log

        sp_table = [[0 for _ in range(n)] for _ in range(k)]
        for i in range(n):
            sp_table[0][i] = arr[i]

        for i in range(1, k):
            for j in range(n - (1 << i) + 1):
                sp_table[i][j] = func(
                    sp_table[i-1][j], sp_table[i-1][j + (1 << (i-1))])
        self.sp_table = sp_table

    def query(self, l, r):
        k = self.bin_log[r-l+1]
        # print(k, L, R-(1<<k)+1)#, self.sp_table[k][L], self.sp_table[k][R-(1<<k)+1])
        return self.func(self.sp_table[k][l], self.sp_table[k][r-(1 << k)+1])


arr = [i for i in range(100)]
spmin = SparseTable(arr, func=min, init=float('inf'))
spmax = SparseTable(arr, func=max, init=float('-inf'))

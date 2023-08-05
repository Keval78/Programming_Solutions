class Solution:
    def merge(self, arr, L, R):
        n, m = len(L), len(R)
        i = j = k = 0
        while i < n and j < m:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < n:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < m:
            arr[k] = R[j]
            j += 1
            k += 1

    def mergesort(self, arr):
        if len(arr) <= 1:
            return
        mid = len(arr)//2
        L, R = arr[:mid], arr[mid:]
        self.mergesort(L)
        self.mergesort(R)
        self.merge(arr, L, R)

    def sortArray(self, nums):
        self.mergesort(nums)
        return nums

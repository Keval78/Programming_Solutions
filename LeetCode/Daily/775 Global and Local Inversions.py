from typing import List


class Solution:
    def merge(self, arr, L, R):
        inv = 0
        n, m = len(L), len(R)
        i = j = k = 0

        while i < n and j < m:
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                inv += n - i
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

        return inv

    def mergesort(self, arr):
        if len(arr) <= 1:
            return 0
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        left_inv = self.mergesort(L)
        right_inv = self.mergesort(R)
        merge_inv = self.merge(arr, L, R)
        return left_inv + right_inv + merge_inv

    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)

        # Using Mergesort: TLE
        # local_inv = 0
        # for i in range(1, n):
        #     if nums[i-1] > nums[i]:
        #         local_inv += 1
        # # print(local_inv)

        # global_inv = self.mergesort(nums)
        # # print(global_inv)
        # return local_inv == global_inv

        for i in range(n):
            if abs(nums[i] - i) > 1:
                return False
        return True

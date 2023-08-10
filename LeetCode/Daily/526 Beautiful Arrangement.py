class Solution:
    def countArrangement(self, n: int) -> int:
        nums = []
        for i in range(1, n+1):
            temp = []
            for j in range(1, n+1):
                if j%i==0 or i%j==0:
                    temp.append(j)
            nums.append(temp)  
        # print(nums)
        perm = [0]
        def bitmask(mask, ind, perm):
            if ind == n:
                perm[0] += 1
            else:
                for val in nums[ind]:
                    if mask & 1<<val == 0:
                        bitmask(mask|(1<<val), ind+1, perm)
        bitmask(0, 0, perm)
        return perm[0]
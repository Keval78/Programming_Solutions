class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1 = cnt2 = 0
        ele1 = ele2 = None
        n = len(nums)

        for num in nums:
            if cnt1 == 0 and ele2 != num:
                ele1 = num
                cnt1 = 1
            elif cnt2 == 0 and ele1 != num:
                ele2 = num
                cnt2 = 1
            elif num == ele1:
                cnt1+=1
            elif num == ele2:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        cnt1 = cnt2 = 0
        for num in nums:
            if num == ele1: cnt1+=1
            elif num == ele2: cnt2+=1
        
        ans = []
        if cnt1 > n//3: ans.append(ele1)
        if cnt2 > n//3: ans.append(ele2)
        return ans

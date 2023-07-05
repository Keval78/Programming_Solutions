"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = root.val
        while root:
            if abs(ans-target) >= abs(root.val-target):
                ans = min(ans, root.val) if abs(ans-target)==abs(target-root.val) else root.val
            # ans = min(root.val, ans, key = lambda x: (abs(target - x), x))
            root = root.left if target < root.val else root.right
        return ans

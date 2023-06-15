'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            inorder_list = []
            def inorder(root, inorder_list):
                if root:
                    inorder(root.left, inorder_list)
                    inorder_list.append(root.val)
                    inorder(root.right, inorder_list)
            inorder(root, inorder_list)
            return inorder_list

    Solution().inorderTraversal()


if __name__ == "__main__":
    main()




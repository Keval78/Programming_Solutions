'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def maxLevelSum(self, root: Optional[TreeNode]) -> int:
            queue, level = [], 1
            currLevel, currSum = 0, -100007
            maxLevel, maxSum = 0, -100007

            queue.append((root, level))
            while len(queue) > 0:
                curr = queue.pop(0)
                #print(curr[0].val, curr[1])
                if currLevel == curr[1]:
                    currSum += curr[0].val
                else:
                    if currSum > maxSum:
                        maxSum = max(maxSum, currSum)
                        maxLevel = curr[1] - 1
                    currLevel = curr[1]
                    currSum = curr[0].val
                    
                #print(currLevel, currSum, maxLevel, maxSum)

                if curr[0].left is not None:
                    queue.append((curr[0].left, curr[1]+1))
                if curr[0].right is not None:
                    queue.append((curr[0].right, curr[1]+1))
            
            if currSum > maxSum:
                maxSum = max(maxSum, currSum)
                maxLevel = currLevel
            #print(currLevel, currSum, maxLevel, maxSum)
            
            return maxLevel

            # #Use of deque and forloop willbe easy.......
            # currLevel, currSum = 0, 0
            # maxLevel, maxSum = 0, float('-inf')

            # queue = collections.deque()
            # queue.append(root)
            # while len(queue) > 0:
            #     currLevel += 1
            #     currSum = 0
            #     for _ in range(len(queue)):
            #         curr = queue.popleft()
            #         currSum += curr.val

            #         if curr.left is not None:
            #             queue.append(curr.left)
            #         if curr.right is not None:
            #             queue.append(curr.right)
            
            #     if currSum > maxSum:
            #         maxSum = currSum
            #         maxLevel = currLevel
          
            # return maxLevel

    Solution().maxLevelSum()


if __name__ == "__main__":
    main()




"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

def main():
    class Solution:
        def maxDistance(self, arrays: List[List[int]]) -> int:
            min_values = [float('inf'), -1]
            max_values = [float('-inf'), -1]
            for i in range(len(arrays)):
                if arrays[i][0] < min_values[0]:
                    min_values[0] = arrays[i][0]
                    min_values[1] = i
                
                if arrays[i][-1] > max_values[0]:
                    max_values[0] = arrays[i][-1]
                    max_values[1] = i
            
            if min_values[1] == max_values[1]:
                new_min, new_max = float('inf'), float('-inf')
                for i in range(len(arrays)):
                    if i!=min_values[1] and arrays[i][0] < new_min:
                        new_min = arrays[i][0]
                for i in range(len(arrays)):
                    if i!=max_values[1] and arrays[i][-1] > new_max:
                        new_max = arrays[i][-1]
                
                return max(new_max-min_values[0], max_values[0]-new_min)
                
            return max_values[0] - min_values[0]
            
    Solution().maxDistance()


if __name__ == "__main__":
    main()

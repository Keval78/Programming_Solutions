'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from collections import defaultdict

def main():
    class Solution:
        def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
            groups, i = {}, 0
            for groupSize in groupSizes:
                if groupSize not in groups:
                    groups[groupSize] = [[i]]
                else:
                    for group in groups[groupSize]:
                        if len(group) != groupSize:
                            group.append(i)
                            break
                    else:
                        groups[groupSize].append([i])
                i+=1
            
            
            # d = defaultdict(list)
            # for i, num in enumerate(groupSizes): d[num].append(i)
            # return [lst[idx:idx + key] for key, lst in d.items() for idx in range(0, len(lst), key)]	

            return [item for sublist in groups.values() for item in sublist]

            
    Solution().groupThePeople(groupSizes = [3,3,3,3,3,1,3])


if __name__ == "__main__":
    main()

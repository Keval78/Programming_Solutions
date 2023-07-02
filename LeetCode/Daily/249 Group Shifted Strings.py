"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from collections import defaultdict

def main():
    class Solution:
        def groupStrings(self, strings: List[str]) -> List[List[str]]:
            # Create a hash value
            def get_hash(string: str):
                key = []
                for a, b in zip(string, string[1:]):
                    key.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
                return ''.join(key)
            
            # Create a hash value (hash_key) for each string and append the string
            # to the list of hash values i.e. mapHashToList["cd"] = ["acf", "gil", "xzc"]
            groups = collections.defaultdict(list)
            for string in strings:
                hash_key = get_hash(string)
                groups[hash_key].append(string)
            
            # Return a list of all of the grouped strings
            return list(groups.values())


    Solution().groupStrings()


if __name__ == "__main__":
    main()

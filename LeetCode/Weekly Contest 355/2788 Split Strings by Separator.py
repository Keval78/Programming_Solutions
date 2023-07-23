class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        vals = []
        for word in words:
            vals.extend(filter(None, word.split(separator)))
        return vals

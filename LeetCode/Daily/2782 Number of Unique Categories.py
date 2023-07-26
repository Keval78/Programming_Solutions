# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        unique = n
        visit = [0]
        for i in range(n):
            val = False
            for j in visit:
                if categoryHandler.haveSameCategory(i, j):
                    val = True
            if not val:
                visit.append(i)
        return len(visit)

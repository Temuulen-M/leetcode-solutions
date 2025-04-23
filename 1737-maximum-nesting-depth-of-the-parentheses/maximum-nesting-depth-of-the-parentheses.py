class Solution:
    def maxDepth(self, s: str) -> int:
        maxNest = 0
        nest = 0

        for x in s:
            if x == "(":
                nest += 1
                maxNest = max(nest, maxNest)
            elif x == ")":
                nest -= 1
        
        return maxNest
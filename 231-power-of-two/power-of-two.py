class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 2
        exp = 0
        while x**exp <= n:
            if x**exp == n:
                return True
            exp += 1
        return False
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        dummy = x
        if dummy < 0:
            dummy *= -1
        while dummy > 0:
            rem = dummy % 10
            result = rem + result * 10
            dummy = dummy // 10
        if x < 0:
            result *= -1
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result

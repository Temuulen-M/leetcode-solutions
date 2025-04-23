class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1

        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_x = 0

        while x_abs != 0:
            digit = x_abs % 10
            x_abs //= 10

            if reversed_x > (INT_MAX - digit) // 10:
                return 0

            reversed_x = reversed_x * 10 + digit

        return sign * reversed_x
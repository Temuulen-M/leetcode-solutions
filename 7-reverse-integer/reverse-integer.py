class Solution:
    def reverse(self, x: int) -> int:
        res = ''
        sign = 1

        if x < 0:
            sign = -1
            x *= -1

        s = str(x)

        for i in s:
            res = i + res

        res = int(res) 

        if res < 2147483647 and res > -2147483648:
            return sign * res
        return 0
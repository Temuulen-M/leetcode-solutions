class Solution:
    def reverse(self, x: int) -> int:
        res = ''
        s = str(x)
        sign = 1

        if s[0] == "-":
            sign = -1
            s = s[1 : ]

        for i in s:
            res = i + res

        res = int(res) 

        if res < 2147483647 and res > -2147483648:
            return sign * res
        return 0
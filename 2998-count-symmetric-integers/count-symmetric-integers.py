class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for x in range(low, high + 1):
            n = str(x)
            l = len(n)
            if l % 2 == 1:
                continue
            ls = sum(int(i) for i in n[ : l//2 ])
            rs = sum(int(i) for i in n[ l//2 : ])
            if ls == rs:
                count += 1
        return count
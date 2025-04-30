from math import factorial
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            subres = []
            for j in range(i + 1):
                # nCr = n!/((n-r)!*r!)
                subres.append(factorial(i)//(factorial(j)*factorial(i-j)))
            res.append(subres)
        return res
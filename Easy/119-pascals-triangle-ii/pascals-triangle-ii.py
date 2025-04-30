class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for j in range(rowIndex + 1):
            # nCr = n!/((n-r)!*r!)
            res.append(factorial(rowIndex)//(factorial(j)*factorial(rowIndex-j)))
        return res
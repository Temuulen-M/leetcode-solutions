class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        low = 1
        high = num // 2

        while low <= high:
            middle = (low + high) // 2
            square = middle * middle

            if square == num:
                return True
            elif square < num:
                low = middle + 1
            else:
                high = middle - 1

        return False
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        rs = s[::-1]
        return s == rs
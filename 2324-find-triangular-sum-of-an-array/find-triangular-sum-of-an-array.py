class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums) - 1
        res = 0
        comb = 1  # C(n, 0) = 1 initially

        for i in range(n + 1):
            res = (res + comb * nums[i]) % 10
            comb = comb * (n - i) // (i + 1)  # Update combination C(n, i+1)

        return res

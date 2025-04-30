class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n  # preallocate result array
        lp, rp = 0, n - 1
        pos = n - 1  # position to fill from right to left

        while lp <= rp:
            if abs(nums[lp]) > abs(nums[rp]):
                res[pos] = nums[lp] ** 2
                lp += 1
            else:
                res[pos] = nums[rp] ** 2
                rp -= 1
            pos -= 1

        return res

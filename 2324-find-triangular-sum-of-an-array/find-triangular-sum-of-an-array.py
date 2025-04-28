class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        temp = []
        for i in range(n - 1):
            res = (nums[i] + nums[i + 1]) % 10
            temp.append(res)
        return self.triangularSum(temp)
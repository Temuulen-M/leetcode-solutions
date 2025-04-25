class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # First apply the operations
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                nums[i - 1] *= 2
                nums[i] = 0
        
        # Move all non-zero elements to the front
        non_zero_pos = 0
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
                non_zero_pos += 1
                
        return nums
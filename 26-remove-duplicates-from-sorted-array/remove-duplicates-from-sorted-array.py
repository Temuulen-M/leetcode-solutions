class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        i = 0  # Pointer for placing unique elements
        for num in nums:
            if num not in seen:
                seen[num] = True
                nums[i] = num
                i += 1
        return i
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        mNum = nums[0]

        for num in nums:
            if num == mNum:
                count += 1
            else:
                count -= 1
            if count == 0:
                mNum = num
                count += 1

        return mNum
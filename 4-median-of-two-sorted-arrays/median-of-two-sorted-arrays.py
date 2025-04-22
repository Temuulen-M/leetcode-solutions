from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLength = len(nums1) + len(nums2)
        medianIndex = totalLength // 2

        currentVal = 0
        prevVal = 0

        count1 = 0
        count2 = 0

        for _ in range(medianIndex + 1):
            prevVal = currentVal
            if count1 < len(nums1) and (count2 >= len(nums2) or nums1[count1] < nums2[count2]):
                currentVal = nums1[count1]
                count1 += 1
            else:
                currentVal = nums2[count2]
                count2 += 1

        if totalLength % 2 == 0:
            return (currentVal + prevVal) / 2
        else:
            return currentVal

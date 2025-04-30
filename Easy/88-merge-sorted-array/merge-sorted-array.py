from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:  # nums2 is empty
            return
        if m == 0:  # nums1 is 'empty'
            for i in range(n):
                nums1[i] = nums2[i]
            return

        counter = 0
        i = 0
        while counter < n and i < m + counter:
            if nums1[i] > nums2[counter]:
                nums1.insert(i, nums2[counter])
                nums1.pop()  # keep size same
                counter += 1
            i += 1

        # If any elements left in nums2, append them
        while counter < n:
            nums1[m + counter] = nums2[counter]
            counter += 1

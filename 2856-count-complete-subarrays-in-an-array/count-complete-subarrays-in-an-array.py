from typing import List
from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_distinct = len(set(nums))
        n = len(nums)

        def count_less_than_k_unique(k):
            count = 0
            left = 0
            freq = defaultdict(int)
            unique = 0

            for right in range(n):
                if freq[nums[right]] == 0:
                    unique += 1
                freq[nums[right]] += 1

                while unique >= k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        unique -= 1
                    left += 1

                count += right - left + 1
            return count

        total_subarrays = n * (n + 1) // 2
        incomplete_subarrays = count_less_than_k_unique(total_distinct)
        return total_subarrays - incomplete_subarrays

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        hashtable = {} # {num : [i, j, ...]}
        count = 0
        
        for i in range(len(nums)):
            if nums[i] in hashtable:
                # For each previous index of the same number
                for prev_idx in hashtable[nums[i]]:
                    # Check if product of indices is divisible by k
                    if (i * prev_idx) % k == 0:
                        count += 1
                hashtable[nums[i]].append(i)
            else:
                hashtable[nums[i]] = [i]
                
        return count
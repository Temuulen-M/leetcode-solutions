class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        hashtable = {} # {num : [i, j, ...]}
        count = 0
        
        for i, n in enumerate(nums):
            if n in hashtable:
                # For each previous index of the same number
                for prev_idx in hashtable[n]:
                    # Check if product of indices is divisible by k
                    if (i * prev_idx) % k == 0:
                        count += 1
                hashtable[n].append(i)
            else:
                hashtable[n] = [i]
                
        return count
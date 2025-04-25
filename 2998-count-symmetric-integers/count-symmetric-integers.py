class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high+1):
            if i < 100 and i % 11 ==0:
                count +=1
            if i> 1000:
                if i // 1000 + i % 1000 // 100 == i % 100 // 10 + i % 10:
                    count += 1
        return count

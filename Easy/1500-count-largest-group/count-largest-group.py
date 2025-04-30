class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = dict() 
        for i in range(1, n+1): 
            summ = self.sum_digits(i) 
            if summ in groups.keys(): 
                groups[summ] += 1
                continue
            groups[summ] = 1
        max_size = max(groups.values())
        return sum(1 for count in groups.values() if count == max_size)
        
    def sum_digits(self, n: int) -> int: 
        summ = 0 
        while n: 
            summ += n % 10 
            n //= 10 
        return summ
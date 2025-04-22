class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [None] * n

        for i in range(n):
            num = i + 1
            if num%3 == 0 and num%5 == 0:
                ans[i] = "FizzBuzz"
            elif num%3 == 0:
                ans[i] = "Fizz"
            elif num%5 == 0:
                ans[i] = "Buzz"
            else:
                ans[i] = str(num)

        return ans
        
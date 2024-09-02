class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        return self.fib(n-2) + self.fib(n -1)
        
# TC- O(2^n) - exponential time complexity

# SC- O(n)
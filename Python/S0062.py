class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            return n * factorial(n - 1)
        total = m + n - 2
        res = factorial(total) // (factorial(m-1) * factorial(n-1))
        return res
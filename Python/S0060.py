class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(n):
            if n == 0 or n == 1: return 1
            return n * factorial(n - 1)
        numbers = [str(i) for i in range(1, n + 1)]
        res = ""
        k -= 1
        while numbers:
            n_left = len(numbers)
            case = factorial(n_left-1)
            index = k // case
            res += numbers[index]
            numbers.pop(index)
            k %= case
        return res
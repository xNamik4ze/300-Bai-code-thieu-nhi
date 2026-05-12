class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 1, 1 
        steps = 1
        while steps < n:
            n2 = n2 + n1
            n1 = n2 - n1
            steps += 1
        return n2
class Solution:
    def mySqrt(self, x: int) -> int: 
        if x < 2:
            return x
        l, r = 2, x // 2
        while l <= r:
            res = l + (r - l) // 2
            product = res * res
            if product > x:
                r = res - 1
            elif product < x:
                l = res + 1
            else:
                return res
        return r
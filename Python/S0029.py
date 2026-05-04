class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        mark1 = -1 if dividend < 0 else 1
        mark2 = -1 if divisor < 0 else 1
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            mul = 1
            temp_div = divisor
            while dividend >= temp_div + temp_div:
                temp_div += temp_div
                mul += mul
            dividend -= temp_div
            res += mul
        mark = mark1 + mark2
        if mark == 0:
            res = 0 - res
        if res < -2**31:
            return -2**31
        elif res > 2**31 - 1:
            return 2**31 - 1
        else:
            return res
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = max_val = 0
        for digit in gain:
            cur += digit
            if cur > max_val:
                max_val = cur
        return max_val

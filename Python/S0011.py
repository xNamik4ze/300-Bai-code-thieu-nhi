class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            long = r - l
            current = long * min(height[l], height[r])
            if current > res: res = current
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
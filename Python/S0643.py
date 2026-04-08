class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = sum(nums[:k])
        max_val = cur
        l, r = 0, k
        for i in range(k, len(nums)):
            cur = cur + nums[i] - nums[i-k]
            if cur > max_val:
                max_val = cur
        return max_val / k
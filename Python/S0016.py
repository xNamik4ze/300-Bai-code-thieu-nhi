class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closet = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            min_sum = nums[i] + nums[i+1] + nums[i+2]
            if min_sum > target:
                if abs(min_sum - target) < abs(closet - target): closet = min_sum
                break
            max_sum = nums[i] + nums[n-1] + nums[n-2]
            if max_sum < target:
                if abs(max_sum - target) < abs(closet - target): closet = max_sum
                continue
            l, r = i + 1, n - 1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if cur_sum == target: return target
                if abs(cur_sum - target) < abs(closet - target): closet = cur_sum
                if cur_sum < target:
                    l += 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                else:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
        return closet 
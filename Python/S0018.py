class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i-1]: continue
            min_i = nums[i] + nums[i+1] + nums[i+2] + nums[i+3]
            if min_i > target: break
            max_i = nums[i] + nums[n-3] + nums[n-2] + nums[n-1]
            if max_i < target: continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]: continue
                min_j = nums[i] + nums[j] + nums[j+1] + nums[j+2]
                if min_j > target: break
                max_j = nums[i] + nums[j] + nums[n-2] + nums[n-1]
                if max_j < target: continue
                l, r = j + 1, n - 1
                while l < r:
                    cur_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if cur_sum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]: l += 1
                        while l < r and nums[r] == nums[r+1]: r -= 1
                    elif cur_sum < target:
                        l += 1
                    else:
                        r -= 1
        return res
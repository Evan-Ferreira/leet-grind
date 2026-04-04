class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = r = used = res = 0
        for r in range(len(nums)):
            used += (nums[r] - nums[r - 1]) * (r - l)
            while l < r and used > k:
                used -= nums[r] - nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = float('inf')
        curr = nums[0]
        while r < len(nums) and r >= l:
            if curr >= target:
                res = min(res, r - l + 1)
                curr -= nums[l]
                l += 1
            else:
                r += 1
                if r < len(nums):
                    curr += nums[r]
        return 0 if res == float('inf') else res
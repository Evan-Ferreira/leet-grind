class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = r = res = 0
        curr = 1
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i])

        while r < len(nums):
            if (prefix[r] // curr) < k:
                res += r - l + 1
                r += 1
            else:
                curr = prefix[l]
                l += 1
            if l > r:
                r = l
        return res
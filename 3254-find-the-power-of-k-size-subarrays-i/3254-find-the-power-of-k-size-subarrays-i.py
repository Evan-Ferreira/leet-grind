class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * (len(nums) - k + 1)
        n = 0
        if k == 1:
            return nums

        for r in range(1, k - 1):
            if (nums[r - 1] + 1) != nums[r]:
                n = r + 1
        for r in range(k - 1, len(nums)):
            if nums[r - 1] + 1  != nums[r]:
                n = min(r, k - 1)
            else:
                n = max(0, n - 1)
            if n > 0:
                res[r - k + 1] = -1
            else:
                res[r -  k + 1] = nums[r]
        
        return res
            
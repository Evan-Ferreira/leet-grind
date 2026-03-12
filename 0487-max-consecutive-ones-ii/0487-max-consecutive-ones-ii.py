class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l1 = l2 = 0
        res = 1

        for r in range(len(nums)):
            if nums[r] == 0:
                l1 = l2
                l2 = r + 1
            res = max(res, r - l1 + 1, r - l2 + 1)
        return res



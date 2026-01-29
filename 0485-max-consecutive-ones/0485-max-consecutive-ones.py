class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        res = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                curr = 0
            res = max(res, curr)
        return res
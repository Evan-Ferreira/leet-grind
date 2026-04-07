class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        # flip = T
        # [0, 1, 1, 0, 1]
        inverse = False
        for i in range(N):
            if (not inverse and nums[i] == 0) or (inverse and nums[i] == 1):
                inverse = not inverse
                res += 1
        return res
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        dp = {0:0}
        res = 0
        total = 0
        for n in nums:
            total += n
            if (total - target) in dp:
                res = max(dp[total - target] + 1, res)
            dp[total] = res
        return res

        
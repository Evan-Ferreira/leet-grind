class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N):
            s = set()
            for j in range(i, N):
                s.add(nums[j])
                res += len(s) ** 2
        return res

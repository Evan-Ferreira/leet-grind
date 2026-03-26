class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        count = defaultdict(int)
        count[0] = 1

        prefix = res = 0
        for i in range(N):
            prefix += nums[i]
            diff = prefix - k
            res += count[diff]
            count[prefix] += 1

        return res
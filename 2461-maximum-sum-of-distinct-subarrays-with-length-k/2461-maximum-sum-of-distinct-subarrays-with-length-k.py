class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        s = res = 0
        numsAmounts = defaultdict(int)

        for i in range(k - 1):
            numsAmounts[nums[i]] += 1
            s += nums[i]

        for r in range(k - 1, len(nums)):
            numsAmounts[nums[r]] += 1
            s += nums[r]

            l = r - k + 1

            if len(numsAmounts) == k:
                res = max(res, s)

            if numsAmounts[nums[l]] == 1:
                del numsAmounts[nums[l]]
            else:
                numsAmounts[nums[l]] -= 1
            s -= nums[l]
            l -= 1
        
        return res
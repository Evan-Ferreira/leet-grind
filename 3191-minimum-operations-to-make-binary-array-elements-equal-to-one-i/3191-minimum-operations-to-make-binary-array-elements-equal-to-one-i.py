class Solution:
    def minOperations(self, nums: List[int]) -> int:
        curr = sum(nums)
        count = 0
        for r in range(2, len(nums)):
            l = r - 2
            if nums[l] == 0:
                prev = sum(nums[l:r + 1])
                for i in range(l, r + 1):
                    nums[i] ^= 1
                new = sum(nums[l:r + 1])
                curr += (new - prev)
                count += 1
        
        return count if curr == len(nums) else -1


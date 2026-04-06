class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for r in range(2, len(nums)):
            l = r - 2
            if nums[l] == 0:
                for i in range(l, r + 1):
                    nums[i] ^= 1
                count += 1
        
        return count if sum(nums) == len(nums) else -1


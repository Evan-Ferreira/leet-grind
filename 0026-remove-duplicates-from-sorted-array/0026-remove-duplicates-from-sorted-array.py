class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = float('inf')
        i = 0
        while i < len(nums):
            if nums[i] == prev:
                del nums[i]
                continue
            prev = nums[i]
            i += 1
        return len(nums)
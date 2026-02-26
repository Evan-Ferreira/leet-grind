class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                minIndex = i
                for j in range(i, len(nums)):
                    if nums[j] < nums[minIndex] and nums[j] > nums[i - 1]:
                        minIndex = j
                nums[i - 1], nums[minIndex] = nums[minIndex], nums[i - 1]
                nums[i:] = nums[i:][::-1]
                return
        nums.reverse()
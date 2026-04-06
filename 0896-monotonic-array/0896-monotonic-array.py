class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        increase = None
        prev = None
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            
            if increase == None:
                if nums[i] > nums[i - 1]:
                    increase = True
                else:
                    increase = False
            elif increase and nums[i] < nums[i - 1] or increase == False and nums[i] > nums[i - 1]:
                return False
        return True
                
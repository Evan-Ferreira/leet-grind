class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []

        for r in range(len(nums)):
            if nums[r] >= 0:
                break

        l = r - 1
        while l >= 0 and r < len(nums):
            if abs(nums[r]) <= abs(nums[l]):
                res.append(nums[r] ** 2)
                r += 1
            else:
                res.append(nums[l] ** 2)
                l -= 1

        for i in range(r, len(nums)):
            res.append(nums[i] ** 2)
        
        for i in range(l, -1, -1):
            res.append(nums[i] ** 2)
        
        return res

        
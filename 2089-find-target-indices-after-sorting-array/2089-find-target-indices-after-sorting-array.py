class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less = 0
        equal = 0
        res = []
        for n in nums:
            if n < target:
                less += 1
            elif n == target:
                equal += 1
        for i in range(equal):
            res.append(less + i)
        return res
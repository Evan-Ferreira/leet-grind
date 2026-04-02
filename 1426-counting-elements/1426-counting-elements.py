class Solution:
    def countElements(self, arr: List[int]) -> int:
        nums = set(arr)
        res = 0

        for num in arr:
            nxt = num + 1
            if nxt in nums:
                res += 1
        return res




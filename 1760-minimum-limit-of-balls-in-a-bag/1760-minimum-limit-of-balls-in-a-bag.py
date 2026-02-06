class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canDivide(max_balls):
            ops = 0
            for n in nums:
                ops += math.ceil(n / max_balls) - 1
                if ops > maxOperations:
                    return False
            return True
        
        l, r = 1, max(nums)
        res = r
        while l <= r:
            m = (l + r) // 2
            if canDivide(m):
                r = m - 1
                res = m
            else:
                l = m + 1
        return res
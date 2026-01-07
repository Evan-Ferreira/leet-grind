class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = []
        for i, num in enumerate(nums):
            curr = 0
            j = 0
            m = float('-inf')
            while num > 0:
                m = max(m, num % 10)
                num = num // 10
                j += 1
            for x in range(j):
                curr += m * 10 ** x
            res.append(curr)
        return sum(res)

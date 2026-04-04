class Solution:
    def arrangeCoins(self, n: int) -> int:
        for i in range(n):
            n -= i + 1
            if n < 0:
                return i
        return n
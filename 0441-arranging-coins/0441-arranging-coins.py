class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1 or n == 0:
            return n

        for i in range(n):
            n -= i + 1
            if n < 0:
                return i
        return n
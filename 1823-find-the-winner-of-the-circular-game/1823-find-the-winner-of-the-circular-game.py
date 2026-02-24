class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def helper(n):
            if n == 1:
                return 0
            
            return (helper(n - 1) + k) % n
        return helper(n) + 1
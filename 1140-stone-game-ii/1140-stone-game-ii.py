class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        dp = {}

        def dfs(l, alice,  m):
            if l == len(piles):
                return 0

            if (l, alice, m) in dp:
                return dp[(l, alice, m)]

            res = 0 if alice else float('inf')
            stones = 0
            for x in range(1, min((2 * m) + 1, N - l + 1)):
                stones += piles[l + x - 1]
                if alice:
                    res = max(res, dfs(l + x, not alice, max(x, m)) + stones)
                else:
                    res = min(res, dfs(l + x, not alice, max(x, m)))

            dp[((l, alice, m))] = res
            return res
        return dfs(0, True, 1)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dp = [[0 for c in range(COLS)] for r in range(ROWS)]

        for r in range(ROWS):
            if r == 0:
                dp[r][0] = grid[r][0]
            else:
                dp[r][0] = grid[r][0] + dp[r - 1][0]
        
        for c in range(COLS):
            if c == 0:
                dp[0][c] = grid[0][c]
            else:
                dp[0][c] = grid[0][c] + dp[0][c - 1]

        for r in range(1, ROWS):
            for c in range(1, COLS):
                dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])

        return dp[ROWS - 1][COLS - 1]


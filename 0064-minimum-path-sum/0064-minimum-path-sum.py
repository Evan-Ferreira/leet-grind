class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        
        for r in range(ROWS):
            dp[r][COLS] = float('inf')
        for c in range(COLS):
            dp[ROWS][c] = float('inf')
        
        dp[ROWS][COLS - 1] = 0
        dp[ROWS - 1][COLS] = 0
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                dp[r][c] = min(dp[r + 1][c], dp[r][c + 1]) + grid[r][c]
        return dp[0][0]
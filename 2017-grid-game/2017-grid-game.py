class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # dp = [[[0, [len(grid[0]), len(grid[0])]] for _ in range(len(grid[0]) + 1)] 
        #         for _ in range(3)]

        # for c in range(len(grid[0]) - 1, -1, -1):
        #     for r in range(1, -1, -1):
        #         if dp[r][c + 1][0] > dp[r + 1][c][0]:
        #             dp[r][c] = [dp[r][c + 1][0] + grid[r][c], [r, c + 1]]
        #         else:
        #             dp[r][c] = [dp[r + 1][c][0] + grid[r][c], [r + 1, c]]
        # r, c = 0, 0

        # while r < len(grid) and c < len(grid[0]):
        #     grid[r][c] = 0
        #     r, c = dp[r][c][1]
        # grid[-1][-1] = 0
        # print(grid)
        # dp = [[[0, [len(grid[0]), len(grid[0])]] for _ in range(len(grid[0]) + 1)] 
        #         for _ in range(3)]
        # for c in range(len(grid[0]) - 1, -1, -1):
        #     for r in range(1, -1, -1):
        #         if dp[r][c + 1][0] > dp[r + 1][c][0]:
        #             dp[r][c] = [dp[r][c + 1][0] + grid[r][c], [r, c + 1]]
        #         else:
        #             dp[r][c] = [dp[r + 1][c][0] + grid[r][c], [r + 1, c]]
        
        # return dp[0][0][0]
        n = len(grid[0])
        
        # Compute prefix sums for efficient range queries
        top_sum = sum(grid[0])
        bottom_sum = 0
        
        result = float('inf')
        
        # Try moving down at each column
        for i in range(n):
            # Before moving down at column i, collect grid[0][i]
            top_sum -= grid[0][i]
            
            # Robot 2's best option: max of remaining top or bottom
            robot2_points = max(top_sum, bottom_sum)
            
            # Robot 1 wants to minimize this
            result = min(result, robot2_points)
            
            # After moving down, we're on bottom row
            bottom_sum += grid[1][i]
        
        return result

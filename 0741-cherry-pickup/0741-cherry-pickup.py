class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dp = {}
        def dfs(r1, c1, c2):
            r2 = r1 + c1 - c2
            if (r1 == N or r2 == N or c1 == N or c2 == N or grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')
            
            if (r1, c1, c2) in dp:
                return dp[(r1, c1, c2)]
            
            if r1 == c1 == N - 1:
                return grid[N - 1][N - 1]
            curr = grid[r1][c1] if (c1 == c2 and r1 == r2) else grid[r1][c1] + grid[r2][c2]
            ans = max(dfs(r1 + 1, c1, c2), dfs(r1, c1 + 1, c2 + 1), 
                dfs(r1 + 1, c1, c2 + 1), dfs(r1, c1 + 1, c2)) + curr 
            dp[(r1, c1, c2)] = ans
            return ans
        res = dfs(0, 0, 0)
        if res == float('-inf'):
            return 0
        else:
            return res
            



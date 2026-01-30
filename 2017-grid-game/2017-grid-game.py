class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        prefix1 = grid[0].copy()
        prefix2 = grid[1].copy()

        for i in range(1, N):
            prefix1[i] += prefix1[i - 1]
            prefix2[i] += prefix2[i - 1]
        
        res = float('inf')
        for i in range(N):
            top = prefix1[-1] - prefix1[i]
            bottom = prefix2[i - 1] if i > 0 else 0
            robot2 = max(top, bottom)
            res = min(res, robot2)

        return res

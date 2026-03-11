class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = [[float('inf') for c in range(COLS)] for r in range(ROWS)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append([r, c, 0])
        if len(q) == (ROWS * COLS) or len(q) == 0:
            return -1
        visited = set()
        while q:
            row, col, dist = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r == ROWS or c == COLS or r < 0 or c < 0 or (r, c) in visited):
                    continue
                visited.add((r, c))
                q.append([r, c, dist + 1])
                res[r][c] = min(res[r][c], dist + 1)

        ans = float('-inf')
        for r in range(ROWS):
            for c in range(COLS):
                ans = max(ans, res[r][c])

        return ans
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        normalized_islands = set()
        visited = set()
        directions = [[0, 1, 'D'], [0, -1, 'U'], [1, 0, "R"], [-1, 0, "L"]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col, markers, direction):
            visited.add((row, col))
            markers.append(direction)
            for dr, dc, d in directions:
                r, c = row + dr, col + dc
                if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visited and grid[r][c] == 1:
                    dfs(r, c, markers, d)
            markers.append('B')  # backtrack

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    markers = []
                    dfs(r, c, markers, 'S')
                    normalized_islands.add(tuple(markers))
        
        return len(normalized_islands)


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        normalized_islands = set()
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(row, col):
            nonlocal visited
            q = deque()
            q.append((row, col))
            local_visited = set()
            local_visited.add((row, col))
            minX, minY = row, col

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r == ROWS or c == COLS or r < 0 or c < 0 or (r, c) in local_visited or grid[r][c] == 0):
                        continue

                    minX = min(r, minX)
                    minY = min(c, minY)
                    local_visited.add((r, c))
                    q.append((r, c))

            visited |= local_visited
            ans = []
            for r, c in local_visited:
                ans.append((r - minX, c - minY))
            
            ans.sort()
            return tuple(ans)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    normalized = bfs(r, c)
                    normalized_islands.add(normalized)
        
        return len(normalized_islands)


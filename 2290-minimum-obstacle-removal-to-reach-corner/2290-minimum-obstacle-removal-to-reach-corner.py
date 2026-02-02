class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        q = collections.deque([(0, 0, 0)])
        visited = set()
        visited.add((0, 0))

        while q:
            obstacles, r, c = q.popleft()

            if (r, c) == (ROWS - 1, COLS - 1):
                return obstacles

            nei = [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]
            for nr, nc in nei:
                if (nr, nc) in visited or nr < 0 or nc < 0 or nr == ROWS or nc == COLS:
                    continue
                
                if grid[nr][nc]:
                    q.append((obstacles + 1, nr, nc))
                else:
                    q.appendleft((obstacles, nr, nc))
                
                visited.add((nr, nc))





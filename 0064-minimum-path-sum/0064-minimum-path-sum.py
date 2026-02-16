class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = [[grid[0][0], [0, 0]]]
        heapq.heapify(q)
        directions = [[1, 0], [0, 1]]
        visited = set()

        while q:
            curr, [row, col] = heapq.heappop(q)

            if (row, col) in visited:
                continue
            
            visited.add((row, col))

            if (row, col) == (ROWS - 1, COLS - 1):
                return curr
            
            for dr, dc in directions:
                r, c = row + dr, col + dc

                if (r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited):
                    continue
                
                heapq.heappush(q, [curr + grid[r][c], [r, c]])
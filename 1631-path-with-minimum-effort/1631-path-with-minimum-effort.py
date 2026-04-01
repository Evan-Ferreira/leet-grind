class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        res = float('inf')

        q = [[0, 0, 0]]
        heapq.heapify(q)

        while q:
            effort, row, col = heapq.heappop(q)
            if (row, col) in visited:
                continue
            visited.add((row, col))

            if row == (ROWS - 1) and col == (COLS - 1):
                return effort

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r == ROWS or c == COLS or r < 0 or c < 0 or 
                    (r, c) in visited):
                    continue
                newEffort = max(abs(heights[row][col] - heights[r][c]), effort)
                heapq.heappush(q, [newEffort, r, c])
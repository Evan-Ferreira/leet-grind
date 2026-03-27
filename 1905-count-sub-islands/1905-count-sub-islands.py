class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        res = 0
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            ans = True
            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or col < 0 or row == ROWS or col == COLS or 
                        (row, col) in visited or grid2[row][col] == 0):
                        continue
                    if grid2[row][col] == 1 and grid1[row][col] == 0:
                        ans = False
                    visited.add((row, col))
                    q.append((row, col))
            return ans
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1 and grid1[r][c] == 1 and (r, c) not in visited:
                    if bfs(r, c):
                        res += 1
        return res
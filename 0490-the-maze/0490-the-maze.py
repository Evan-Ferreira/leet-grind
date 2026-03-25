class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        ROWS, COLS = len(maze), len(maze[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        r, c = start

        def dfs(r, c):
            if (r, c) in visited:
                return False
            
            if [r, c] == destination:
                return True
            
            visited.add((r, c))

            for dr, dc in directions:
                row, col = r, c
                while (row >= 0 and col >= 0 and row < ROWS and col < COLS and maze[row][col] == 0):
                    row, col = row + dr, col + dc
                
                if dfs(row - dr, col - dc):
                    return True
            
            return False
        return dfs(r, c)


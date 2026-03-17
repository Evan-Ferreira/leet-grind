class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        ROWS, COLS = m, n
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        walls = {(r, c) for (r, c) in walls}
        seen = set()

        for r, c in guards:
            walls.add((r, c))
        
        for r, c in guards:
            for dr, dc in directions:
                row, col = r + dr, c + dc
                while not ((row, col) in walls or row < 0 or col < 0 or row == ROWS or col == COLS):
                    seen.add((row, col))
                    row += dr
                    col += dc
        
        return (ROWS * COLS) - len(walls | seen)

        


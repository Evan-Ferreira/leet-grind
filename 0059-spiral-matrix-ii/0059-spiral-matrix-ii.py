class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ROWS = COLS = n
        MIN_ROWS = MIN_COLS = row = col = 0
        curr = 1
        
        while curr <= (n * n):
            res[MIN_ROWS][MIN_COLS] = curr
            for dr, dc in directions:
                row, col = row + dr, col + dc
                while (row < ROWS and col < COLS and row >= MIN_ROWS 
                    and col >= MIN_COLS and res[row][col] == 0):
                    curr += 1
                    res[row][col] = curr
                    row, col = row + dr, col + dc
                row, col = row - dr, col - dc
                
            MIN_ROWS += 1
            MIN_COLS += 1
            ROWS -= 1
            COLS -= 1
            row, col = MIN_ROWS, MIN_COLS
            curr += 1
        return res
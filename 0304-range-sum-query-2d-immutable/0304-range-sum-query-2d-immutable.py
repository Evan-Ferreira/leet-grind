class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        self.sum_matrix = [[0] * self.COLS for _ in range(self.ROWS)]
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if c > 0:
                    self.sum_matrix[r][c] = self.sum_matrix[r][c - 1] + matrix[r][c]
                else:
                    self.sum_matrix[r][c] = matrix[r][c]
        for c in range(self.COLS):
            for r in range(1, self.ROWS):
                self.sum_matrix[r][c] += self.sum_matrix[r - 1][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        first_sum = self.sum_matrix[row2][col2]
        left_sum = 0 if col1 == 0 else self.sum_matrix[row2][col1 - 1]
        right_sum = 0 if row1 == 0 else self.sum_matrix[row1 - 1][col2]
        add_back = 0 if (row1 == 0 or col1 == 0) else self.sum_matrix[row1 - 1][col1  - 1]
        return first_sum - left_sum - right_sum + add_back
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
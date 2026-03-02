class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])
        res = 0

        for r in range(ROWS):
            if r == (ROWS // 2) and ROWS % 2 == 1:
                continue
            res += mat[r][r]
        
        for r in range(ROWS):
            res += mat[r][ROWS - r - 1]
        
        return res
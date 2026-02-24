class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = set()

        for r in range(ROWS):
            minC = 0
            for c in range(COLS):
                if matrix[r][c] < matrix[r][minC]:
                    minC = c
            prevR = r
            maxR = r
            for r in range(ROWS):
                if matrix[r][minC] > matrix[maxR][minC]:
                    maxR = r
            if maxR == prevR:
                res.add(matrix[prevR][minC])
        
        return list(res)

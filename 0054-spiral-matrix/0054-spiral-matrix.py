class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        endRow, endCol = len(matrix) - 1, len(matrix[0]) - 1
        startRow = startCol = 0
        res = []
        state = 'right'

        while len(res) != (len(matrix) * len(matrix[0])):
            if state == 'right':
                for c in range(startCol, endCol + 1):
                    res.append(matrix[startRow][c])
                state = 'down'
            elif state == 'down':
                for r in range(startRow + 1, endRow):
                    res.append(matrix[r][endCol])
                state = 'left'
            elif state == 'left':
                for c in range(endCol, startCol - 1, -1):
                    res.append(matrix[endRow][c])
                state = 'up'
            else:
                for r in range(endRow - 1, startRow, -1):
                    res.append(matrix[r][startCol])
                state = 'right'
                startRow += 1
                endRow -= 1
                startCol += 1
                endCol -= 1
        return res


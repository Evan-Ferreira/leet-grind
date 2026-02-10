class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = 0
        prev_heights = [0] * COLS

        for r in range(ROWS):
            heights = matrix[r][:]
            for c in range(COLS):
                if heights[c] > 0:
                    heights[c] += prev_heights[c]
            
            sorted_heights = sorted(heights, reverse=True)
            for c in range(COLS):
                res = max(res, (c + 1) * sorted_heights[c])
            prev_heights = heights
        return res
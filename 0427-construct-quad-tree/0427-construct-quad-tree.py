"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(startR, startC, endR, endC):
            # Check if all cells in this region have the same value
            val = grid[startR][startC]
            isLeaf = True
            
            for r in range(startR, endR):
                for c in range(startC, endC):
                    if grid[r][c] != val:
                        isLeaf = False
                        break
                if not isLeaf:
                    break
            
            if isLeaf:
                return Node(val, True, None, None, None, None)
            
            # Divide into 4 quadrants
            midR = (startR + endR) // 2
            midC = (startC + endC) // 2
            
            topLeft = dfs(startR, startC, midR, midC)
            topRight = dfs(startR, midC, midR, endC)
            bottomLeft = dfs(midR, startC, endR, midC)
            bottomRight = dfs(midR, midC, endR, endC)
            
            # Check if all 4 children are leaves with the same value
            if (topLeft.isLeaf and topRight.isLeaf and 
                bottomLeft.isLeaf and bottomRight.isLeaf and
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return Node(topLeft.val, True, None, None, None, None)
            
            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(0, 0, ROWS, COLS)
            
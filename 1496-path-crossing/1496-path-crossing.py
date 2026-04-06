class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        directions = {
            "N": [0, 1],
            "E": [1, 0],
            "W": [-1, 0],
            "S": [0, -1]
        }
        x, y = 0, 0
        visited.add((x, y))
        for p in path:
            dr, dc = directions[p] 
            next_x, next_y = x + dr, y + dc
            if (next_x, next_y) in visited:
                return True
            visited.add((next_x, next_y))
            x, y = next_x, next_y
        return False
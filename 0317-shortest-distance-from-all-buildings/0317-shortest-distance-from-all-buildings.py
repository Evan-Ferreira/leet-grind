class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]          
        ROWS, COLS = len(grid), len(grid[0])
        buildings = 0
        res = float('inf')

        def bfs(grid, distances, row, col):
            # Use a queue to do a BFS, starting from cell at (row, col)
            q = collections.deque()
            q.append([row, col, 0])
            # Keep track of visited cells
            visited = set()
            visited.add((row, col))
            steps = 0
            
            while q:
                # Record the cells that we will explore in the next level
                row, col, dst = q.popleft()

                # If we reached an empty cell, then add the distance
                # and increment the count of houses reached at this cell
                if grid[row][col] == 0:
                    distances[row][col][1] += 1
                
                # Traverse the next cells which is not a blockage
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    
                    if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) 
                        in visited or grid[r][c] != 0):
                        continue
                    distances[r][c][0] += dst + 1 
                    q.append((r, c, dst + 1))
                    visited.add((r, c))
        
        # Store [total_dist, houses_count] for each cell
        distances = [[[0, 0] for _ in range(COLS)] for _ in range(ROWS)]
        
        # Count houses and start BFS from each house
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    buildings += 1
                    bfs(grid, distances, row, col)
        
        # Check all empty lands with houses count equal to total houses and find the min ans
        for row in range(ROWS):
            for col in range(COLS):
                if distances[row][col][1] == buildings:
                    res = min(res, distances[row][col][0])
        
        # If we haven't found a valid cell return -1
        if res == float('inf'):
            return -1
        
        return res
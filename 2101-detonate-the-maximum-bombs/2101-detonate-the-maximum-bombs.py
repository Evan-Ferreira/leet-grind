class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        N = len(bombs)
        adj = defaultdict(list)

        for i in range(N):
            x1, y1, r1 = bombs[i]
            for j in range(i + 1, N):
                x2, y2, r2 = bombs[j]
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                if r1 >= distance:
                    adj[i].append(j)
                if r2 >= distance:
                    adj[j].append(i)
        
        
        def dfs(node):
            if self.visited == N:
                return 0
            
            self.visited.add(node)
            res = 1
            for nei in adj[node]:
                if nei not in self.visited:
                    res += dfs(nei)
            return res

        res = 1
        
        for i in range(N):
            self.visited = set()
            res = max(res, dfs(i))
        
        return res

                
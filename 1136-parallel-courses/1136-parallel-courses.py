class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = defaultdict(list)

        
        for prev, nxt in relations:
            adj[prev].append(nxt)
        
        visited = set()
        m = {}

        def dfs(crs):
            if crs in visited:
                return float("inf")
            
            if crs in m:
                return m[crs]
            
            visited.add(crs)
            res = 1
            for nxt in adj[crs]:
                res = max(res, dfs(nxt) + 1)
            visited.remove(crs)
            m[crs] = res
            return res
        
        res = float("-inf")
        for crs in range(1, n + 1):
            tmp = dfs(crs)
            if tmp == float('inf'):
                return - 1
            res = max(res, tmp)
        
        return res
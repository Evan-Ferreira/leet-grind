class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        res = 0
        edges = { (a, b) for a, b in connections }
        for start, dest in connections:
            adj[start].append(dest)
            adj[dest].append(start)

        visited = set()
        def dfs(node):
            nonlocal res

            visited.add(node)
            for nei in adj[node]:
                if nei in visited:
                    continue
                
                if (nei, node) not in edges:
                    res += 1
                
                dfs(nei)
        dfs(0)
        return res
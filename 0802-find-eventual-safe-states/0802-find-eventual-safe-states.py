class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        dp = {}
        visited = set()
        def dfs(node):
            if node in visited:
                return False
                
            if node in dp:
                return dp[node]

            if len(graph[node]) == 0:
                return True

            dp[node] = True
            visited.add(node)
            for nei in graph[node]:
                dp[node] = dp[node] and dfs(nei)
            visited.remove(node)
            return dp[node]

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        
        return res


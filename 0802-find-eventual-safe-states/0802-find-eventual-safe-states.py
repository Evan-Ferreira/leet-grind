class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        dp = {}
        visited = set()
        def dfs(node):
            if node in visited:
                return False

            if len(graph[node]) == 0:
                return True

            ans = True
            visited.add(node)
            for nei in graph[node]:
                ans = ans and dfs(nei)
            visited.remove(node)
            if ans:
                graph[node] = []
            return ans

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        
        return res


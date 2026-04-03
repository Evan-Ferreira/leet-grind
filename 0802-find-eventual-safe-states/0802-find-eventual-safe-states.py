class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        def dfs(node):
            if node in visited:
                return False

            if len(graph[node]) == 0:
                return True

            visited.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited.remove(node)
            graph[node] = []
            return True

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        
        return res


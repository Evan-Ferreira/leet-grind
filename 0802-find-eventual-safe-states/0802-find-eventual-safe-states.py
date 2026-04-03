class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}
        def dfs(node):
            if node in safe:
                return safe[node]

            if len(graph[node]) == 0:
                return True

            safe[node] = False
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            safe[node] = True
            return True

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        
        return res


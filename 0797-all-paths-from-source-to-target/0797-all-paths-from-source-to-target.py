class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        res = []
        curr = []

        def dfs(i):
            if i == N - 1:
                curr.append(i)
                res.append(curr.copy())
                curr.pop()
                return
            
            curr.append(i)
            for node in graph[i]:
                dfs(node)
            curr.pop()
        dfs(0)
        return res
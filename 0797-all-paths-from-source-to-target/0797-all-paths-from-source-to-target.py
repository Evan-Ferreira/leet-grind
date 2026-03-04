class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        self.res = []
        self.curr = []

        def dfs(i):
            if i == N - 1:
                self.curr.append(i)
                self.res.append(self.curr.copy())
                self.curr.pop()
                return
            
            self.curr.append(i)
            for node in graph[i]:
                dfs(node)
            self.curr.pop()
        dfs(0)
        return self.res
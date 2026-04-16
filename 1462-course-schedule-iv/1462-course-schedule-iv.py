class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[crs].append(pre)
        
        crsReqs = defaultdict(set)

        def dfs(crs):
            nonlocal crsReqs
            for pre in adj[crs]:
                if pre in crsReqs:
                    crsReqs[crs].add(pre)
                    crsReqs[crs] |= crsReqs[pre]
                else:
                    crsReqs[crs].add(pre)
                    dfs(pre)
                    crsReqs[crs] |= crsReqs[pre]
                    

        res = []
        for pre, crs in queries:
            if crs not in crsReqs:
                dfs(crs)
            res.append(True if pre in crsReqs[crs] else False)
        return res
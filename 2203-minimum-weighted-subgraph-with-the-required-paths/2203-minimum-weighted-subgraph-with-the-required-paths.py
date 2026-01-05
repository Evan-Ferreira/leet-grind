class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        adj1 = { i:[] for i in range(n)}
        adj2 = { i:[] for i in range(n)}

        for src, dst, w in edges:
            adj1[src].append([w, dst])
            adj2[dst].append([w, src])

        def dijkstras(graph, src):
            hp = [[0, src]]
            heapq.heapify(hp)
            shortest = {}

            while hp:
                w1, n1 = heapq.heappop(hp)
                if n1 in shortest:
                    continue
                
                shortest[n1] = w1
                for w2, n2 in graph[n1]:
                    if n2 not in shortest:
                        heapq.heappush(hp, [w1 + w2, n2])
            
            return [shortest.get(i, float("inf")) for i in range(n)]

        arr1 = dijkstras(adj1, src1)
        arr2 = dijkstras(adj1, src2)
        arr3 = dijkstras(adj2, dest)

        ans = float("inf")
        for i in range(n):
            ans = min(ans, arr1[i] + arr2[i] + arr3[i])
        
        return -1 if ans == float('inf') else ans
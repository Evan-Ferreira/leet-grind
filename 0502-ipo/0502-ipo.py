class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        profits, capital = zip(*sorted(zip(profits, capital)))

        capitalD = defaultdict(list)
        for i in range(len(profits)):
            capitalD[capital[i]].append(profits[i])

        capital = sorted(set(capital))
        N = len(capital)

        currCapital = w
        i = 0
        heap = []

        for _ in range(min(k, len(profits))):
            while i < N and capital[i] <= currCapital:
                for p in capitalD[capital[i]]:
                    heapq.heappush_max(heap, p)
                del capitalD[capital[i]]
                i += 1

            if heap:
                currCapital += heapq.heappop_max(heap)
            else:
                break
            
        return currCapital
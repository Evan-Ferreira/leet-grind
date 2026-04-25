class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: (x[1], x[2]))
        seen = []
        curr = 0
        for i in range(len(trips)):
            curr += trips[i][0]
            while seen and seen[0][0] <= trips[i][1]:
                curr -= heapq.heappop(seen)[1]
            heapq.heappush(seen, [trips[i][2], trips[i][0]])
            if curr > capacity:
                return False
        return True

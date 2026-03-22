class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        h = [int(n) for n in nums]
        heapq.heapify_max(h)
        res = 0
        for _ in range(k):
            res = heapq.heappop_max(h)
        
        return str(res)



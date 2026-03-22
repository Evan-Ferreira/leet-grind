class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        h = []
        for n in nums:
            heapq.heappush_max(h, int(n))
        
        res = 0
        for _ in range(k):
            res = heapq.heappop_max(h)

        return str(res)

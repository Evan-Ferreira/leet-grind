class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        b = bricks
        l = ladders
        prev_heights = []
        
        for i in range(len(heights)):
            if i == len(heights) - 1:
                break
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            heapq.heappush_max(prev_heights, diff)
            if diff <= b:
                b -= diff
            else:
                while l and prev_heights and b < diff:
                    b += heapq.heappop_max(prev_heights)
                    l -= 1
                if b >= diff:
                    b -= diff
                else:
                    break

        return i
            

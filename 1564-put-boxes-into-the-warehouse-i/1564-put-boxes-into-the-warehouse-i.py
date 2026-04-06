class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # positive int[]: boxes, warehouses
        # boxes: width = 1, height[i]
        # warehouses: height of room i is warehouse[i], labelled from 0 to n - 1
        boxes.sort(reverse = True)
        i = 0
        count = 0

        for room in warehouse:
            while i < len(boxes) and boxes[i] > room:
                i += 1
            
            if i == len(boxes):
                return count
            
            count += 1
            i += 1
        return count
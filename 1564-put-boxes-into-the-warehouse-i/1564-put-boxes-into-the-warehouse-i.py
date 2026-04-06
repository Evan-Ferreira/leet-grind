class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # positive int[]: boxes, warehouses
        # boxes: width = 1, height[i]
        # warehouses: height of room i is warehouse[i], labelled from 0 to n - 1
        boxes.sort()
        j = 0
        res = 0
        N = len(warehouse)

        warehouse_mins = [0] * N
        warehouse_mins[0] = warehouse[0]

        for i in range(1, N):
            if warehouse[i] < warehouse_mins[i - 1]:
                warehouse_mins[i] = warehouse[i]
            else:
                warehouse_mins[i] = warehouse_mins[i - 1]
        
        for i in range(N - 1, -1 , -1):
            if j < len(boxes) and warehouse_mins[i] < boxes[j]:
                continue
            if j < len(boxes) and boxes[j] <= warehouse_mins[i]:
                j += 1
                res += 1
        return res
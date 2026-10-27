class StockPrice:
    def __init__(self):
        self.mxheap = []
        self.mnheap = []
        self.timeToNode = {}
        self.latestTime = 0
        self.latestPrice = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timeToNode:
            self.timeToNode[timestamp][2] = False

        if timestamp >= self.latestTime:
            self.latestTime = timestamp
            self.latestPrice = price

        node = [price, timestamp, True]
        self.timeToNode[timestamp] = node
        heapq.heappush_max(self.mxheap, node)
        heapq.heappush(self.mnheap, node)

    def current(self) -> int:
        return self.latestPrice

    def maximum(self) -> int:
        while self.mxheap[0][2] == False:
            heapq.heappop_max(self.mxheap)
        return self.mxheap[0][0]

    def minimum(self) -> int:
        while self.mnheap[0][2] == False:
            heapq.heappop(self.mnheap)
        return self.mnheap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
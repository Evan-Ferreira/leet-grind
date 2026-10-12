class HitCounter:
    def __init__(self):
        self.count = 0
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        self.count += 1
        if self.queue and self.queue[-1][0] == timestamp:
            self.queue[-1][1] += 1
        else:
            self.queue.append([timestamp, 1]) 

    def getHits(self, timestamp: int) -> int:
        while self.queue and (timestamp - self.queue[0][0]) >= 300:
            _, val = self.queue.popleft()
            self.count -= val
        return self.count

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
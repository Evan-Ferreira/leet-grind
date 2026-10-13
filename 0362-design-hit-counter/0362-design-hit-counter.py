class HitCounter:
    def __init__(self):
        self.q = deque()
        self.count = 0

    def hit(self, timestamp: int) -> None:
        if self.q and self.q[-1][0] == timestamp:
            self.q[-1][1] += 1
        else:
            self.q.append([timestamp, 1])
        self.count += 1
        
    def getHits(self, timestamp: int) -> int:
        while self.q and (timestamp - self.q[0][0]) >= 300:
            self.count -= self.q.popleft()[1]
        return self.count
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
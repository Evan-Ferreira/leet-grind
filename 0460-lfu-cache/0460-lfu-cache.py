class LFUCache:
    def __init__(self, capacity: int):
        self.heap = []
        heapq.heapify(self.heap)
        self.cache = defaultdict(list)
        self.capacity = capacity
        self.time = 0

    def get(self, key: int) -> int:
        self.time += 1
        if key not in self.cache:
            return -1
        
        count, prevTime, k, v = self.cache[key]
        self.cache[key][0] = count + 1
        self.cache[key][1] = self.time
        heapq.heapify(self.heap)
        return v

        

    def put(self, key: int, value: int) -> None:
        self.time += 1

        if key in self.cache:
            count, prevTime, oldValue, _ = self.cache[key]
            self.cache[key][0] = count + 1
            self.cache[key][1] = self.time
            self.cache[key][3] = value
            heapq.heapify(self.heap)
            return
        
        if len(self.cache) == self.capacity:
            count, prevTime, k, v = heapq.heappop(self.heap)
            del self.cache[k]
        
        new = [1, self.time, key, value]
        self.cache[key] = new
        heapq.heappush(self.heap, new)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
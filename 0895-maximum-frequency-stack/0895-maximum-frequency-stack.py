class FreqStack:
    def __init__(self):
        self.heap = []
        self.nodeToTime = defaultdict(list)
        self.nodeToHeap = {}
        self.time = 0

    def push(self, val: int) -> None:
        if val not in self.nodeToHeap:
            node = [1, self.time, val]
            self.nodeToHeap[val] = node
            heapq.heappush_max(self.heap, node)
            self.time += 1
            return
        
        freq, t, _ = self.nodeToHeap[val]
        self.nodeToTime[val].append(t)
        self.nodeToHeap[val][0] += 1
        self.nodeToHeap[val][1] = self.time
        heapq.heapify_max(self.heap)
        self.time += 1

    def pop(self) -> int:
        freq, _, val = self.heap[0]
        if freq == 1:
            if val in self.nodeToTime and self.nodeToTime[val]:
                del self.nodeToTime[val]
            del self.nodeToHeap[val]
            self.time += 1
            heapq.heappop_max(self.heap)
            return val
        
        self.nodeToHeap[val][0] -= 1
        t = self.nodeToTime[val].pop()
        self.nodeToHeap[val][1] = t
        heapq.heapify_max(self.heap)
        return val
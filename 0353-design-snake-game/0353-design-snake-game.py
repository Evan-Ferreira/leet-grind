class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.stack = [f for f in food[::-1]]
        self.bodySet = set([(0, 0)])
        self.bodyQ = deque([(0, 0)])
        self.head = [0, 0]
        print(self.stack)
        self.foodR, self.foodC = self.stack.pop()

    def move(self, direction: str) -> int:
        if direction == "U":
            self.head[0] -= 1
        elif direction == "D":
            self.head[0] += 1
        elif direction == "L":
            self.head[1] -= 1
        else:
            self.head[1] += 1

        if self.head[0] != self.foodR or self.head[1] != self.foodC:
            tailR, tailC = self.bodyQ.popleft()
            self.bodySet.remove((tailR, tailC))
        elif self.stack:
            self.foodR, self.foodC = self.stack.pop()
        else:
            self.foodR, self.foodC = -1, -1

        if ((self.head[0], self.head[1]) in self.bodySet or self.head[0] < 0 or self.head[0] == self.height or self.head[1] < 0 or self.head[1] == self.width):
            return -1
        
        self.bodySet.add((self.head[0], self.head[1]))
        self.bodyQ.append([self.head[0], self.head[1]])
        
        return len(self.bodyQ) - 1

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
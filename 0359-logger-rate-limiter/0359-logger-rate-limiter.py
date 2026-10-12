class Logger:

    def __init__(self):
        self.seen = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if (message in self.seen and (timestamp - self.seen[message]) >= 10) or message not in self.seen:
            self.seen[message] = timestamp
            return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
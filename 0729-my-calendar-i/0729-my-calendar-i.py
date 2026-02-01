class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.events:
            self.events.append([startTime, endTime])
            return True

        if len(self.events) == 1:
            if endTime <= self.events[0][0]:
                self.events.insert(0, [startTime, endTime])
            elif startTime >= self.events[0][1]:
                self.events.insert(1, [startTime, endTime])
            else:
                return False
            return True
        
        if endTime <= self.events[0][0]:
            self.events.insert(0, [startTime, endTime])
            return True

        for i in range(1, len(self.events)):
            preS, preE = self.events[i - 1][0], self.events[i - 1][1]
            postS, postE = self.events[i][0], self.events[i][1]
            
            if preE <= startTime and endTime <= postS:
                self.events.insert(i, [startTime, endTime])
                return True

            if startTime >= postE:
                continue
            
            return False

        self.events.append([startTime, endTime])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
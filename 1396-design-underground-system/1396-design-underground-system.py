class UndergroundSystem:

    def __init__(self):
        # (start_station, endStation) ] = [cumulativeTime, numOfPeopel]
        self.timeMap = defaultdict(list)
        # customerId = [start_station, check_in_time]
        self.checkInMap = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, checkInTime = self.checkInMap[id]
        if not self.timeMap[(startStation, stationName)]:
            self.timeMap[(startStation, stationName)] = [t - checkInTime, 1]
        else:
            cumTime, numOfPeople = self.timeMap[(startStation, stationName)]
            self.timeMap[(startStation, stationName)] = [(t - checkInTime) + cumTime, numOfPeople + 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        cumTime, numOfPeople = self.timeMap[(startStation, endStation)]
        return cumTime / numOfPeople


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
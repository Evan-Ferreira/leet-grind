class Leaderboard:

    def __init__(self):
        self.A = collections.Counter()

    def addScore(self, playerId, score):
        self.A[playerId] += score

    def top(self, K):
        return sum(v for i,v in self.A.most_common(K))

    def reset(self, playerId):
        self.A[playerId] = 0
    

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
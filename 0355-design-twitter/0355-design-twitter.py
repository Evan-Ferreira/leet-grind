class Twitter:
    def __init__(self):
        self.whoUserFollows = defaultdict(set)
        self.userTweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.whoUserFollows[userId]:
            self.whoUserFollows[userId].add(userId)
        self.time += 1
        self.userTweets[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> list[int]:
        ans = []
        followerToIndex = {}
        for _ in range(10):
            currMinTime = float('-inf')
            currTweet = ""
            followerUsed = 0
            for followerId in self.whoUserFollows[userId]:
                tweets = self.userTweets[followerId]
                if followerId not in followerToIndex:
                    followerToIndex[followerId] = len(tweets) - 1
                
                i = followerToIndex[followerId]
                if i == -1:
                    continue

                if tweets[i][0] > currMinTime:
                    currMinTime = tweets[i][0]
                    followerUsed = followerId
                    currTweet = tweets[i][1]
            
            if currMinTime != float('-inf'):
                ans.append(currTweet)
                followerToIndex[followerUsed] -= 1
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.whoUserFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.whoUserFollows[followerId]: 
            self.whoUserFollows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
import heapq

class Twitter(object):

    def __init__(self):
        self.timer = 0
        self.tweets = {}     # userId -> list of (time, tweetId)
        self.following = {}  # userId -> set of followeeIds

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweets.setdefault(userId, []).append((self.timer, tweetId))
        self.timer -= 1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        heap = []
        users = self.following.get(userId, set()) | {userId}

        for u in users:
            if u in self.tweets:
                idx = len(self.tweets[u]) - 1
                if idx >= 0:
                    time, tweetId = self.tweets[u][idx]
                    heapq.heappush(heap, (time, tweetId, u, idx - 1))

        result = []
        while heap and len(result) < 10:
            time, tweetId, u, idx = heapq.heappop(heap)
            result.append(tweetId)
            if idx >= 0:
                ntime, ntweetId = self.tweets[u][idx]
                heapq.heappush(heap, (ntime, ntweetId, u, idx - 1))

        return result

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.following.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.following:
            self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
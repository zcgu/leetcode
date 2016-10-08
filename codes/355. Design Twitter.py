class Twitter(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweet = {}
        self.follows = {}
        self.time = 0
        
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId in self.tweet:
            self.tweet[userId].append((tweetId, self.time))
        else:
            self.tweet[userId] = [(tweetId, self.time)]
        
        self.follow(userId, userId)
        
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.follows:
            return []
            
        tmp = []
        
        for followee in self.follows[userId]:
            if followee in self.tweet:
                tmp += self.tweet[followee][-10:]
        
        tmp.sort(key=lambda l: l[1])
        
        return [x for x, y in reversed(tmp[-10:])]
        
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = set([followeeId])

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
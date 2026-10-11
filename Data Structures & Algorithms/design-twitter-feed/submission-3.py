class Twitter:
    def __init__(self):
        self.followed = defaultdict(lambda: set())
        self.posts = defaultdict(lambda: [])
        self.post_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.post_count, tweetId))
        # The news feed fetches at most the 10 most recent tweets,
        # so we don't need to save more than 10 posts per user.
        self.posts[userId] = self.posts[userId][-10:]
        self.post_count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed_heap = []
        # Users see their own posts in their feed.
        self.followed[userId].add(userId)
        # And the posts of everyone they follow.
        for followeeId in self.followed[userId]:
            for post in self.posts[followeeId]:
                post_count, tweetId = post
                # The post count (timestamp) is negated so that Python's
                # min heap can later be used as a max heap.
                heapq.heappush(news_feed_heap, (-post_count, tweetId))
        
        news_feed = []
        for _ in range(min(10, len(news_feed_heap))):
            _, tweetId = heapq.heappop(news_feed_heap)
            news_feed.append(tweetId)

        return news_feed
            

    def follow(self, followerId: int, followeeId: int) -> None:
        assert followerId != followeeId
        self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followed[followerId]:
            self.followed[followerId].remove(followeeId)

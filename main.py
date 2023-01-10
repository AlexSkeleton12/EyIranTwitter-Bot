from eventTriggers import *

print(reddit.user.me())

tweet1 = API.user_timeline(screen_name=acc1, count=1)[0]
tweet2 = API.user_timeline(screen_name=acc2, count=1)[0]
tweet3 = API.user_timeline(screen_name=acc3, count=1)[0]
tweet4 = API.user_timeline(screen_name=acc4, count=1)[0]
tweet5 = API.user_timeline(screen_name=acc5, count=1)[0]
tweet6 = API.user_timeline(screen_name=acc6, count=1)[0]
tweet7 = API.user_timeline(screen_name=acc7, count=1)[0]
tweet8 = API.user_timeline(screen_name=acc8, count=1)[0]

latestTweet1 = tweet1
latestTweet2 = tweet2
latestTweet3 = tweet3
latestTweet4 = tweet4
latestTweet5 = tweet5
latestTweet6 = tweet6
latestTweet7 = tweet7
latestTweet8 = tweet8

eventLoop(latestTweet1, latestTweet2, latestTweet3, latestTweet4, latestTweet5, latestTweet6, latestTweet7, latestTweet8, tweet1, tweet2, tweet3, tweet4, tweet5, tweet6, tweet7, tweet8)
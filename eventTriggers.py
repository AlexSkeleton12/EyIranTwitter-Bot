import tweepy
import praw
from urlextract import URLExtract
from time import sleep

from keysnshit import twitterKeys, redditKeys

auth = tweepy.OAuth1UserHandler(
   twitterKeys["ConsumerKey"], twitterKeys["ConsumerKeySecret"], twitterKeys["AccessKey"], twitterKeys["AccessKeySecret"]
)

API = tweepy.API(auth)

reddit = praw.Reddit(
    client_id=redditKeys["PUS"],
    client_secret=redditKeys["Secret"],
    password=redditKeys["Password"],
    user_agent="EyIranTwitter-Bot by u/AlexShadDynasty",
	ratelimit_seconds=1,
    username=redditKeys["Username"]
)

extractor = URLExtract()

def eventSource1(latestTweet1, tweet1):
	if latestTweet1 != tweet1:
    	# Trigger Reddit Post
		print(acc1)
		if len(API.user_timeline(screen_name=acc1, count=1)[0].entities["urls"][0]["expanded_url"]) == 0:
			reddit.subreddit("EyIran").submit(title=tweet1.text)
		elif len(API.user_timeline(screen_name=acc1, count=1)[0].entities["urls"][0]["expanded_url"]) != 0:
			reddit.subreddit("EyIran").submit(title=tweet1.text, url=API.user_timeline(screen_name=acc1, count=1)[0].entities["urls"][0]["expanded_url"])
        # Reset Loop
		latestTweet1 = tweet1

	return latestTweet1

def eventSource2(latestTweet2, tweet2):
	if latestTweet2 != tweet2:
    	# Trigger Reddit Post
		print(acc2)
		if len(API.user_timeline(screen_name=acc2, count=1)[0].entities["urls"][0]["expanded_url"]) == 0:
			reddit.subreddit("EyIran").submit(title=tweet2.text)
		elif len(API.user_timeline(screen_name=acc2, count=1)[0].entities["urls"][0]["expanded_url"]) != 0:
			reddit.subreddit("EyIran").submit(title=tweet2.text, url=API.user_timeline(screen_name=acc2, count=1)[0].entities["urls"][0]["expanded_url"])
        # Reset Loop
		latestTweet2 = tweet2

	return latestTweet2

def eventSource3(latestTweet3, tweet3):
	if latestTweet3 != tweet3:
    	# Trigger Reddit Post
		print(acc3)
		if len(API.user_timeline(screen_name=acc3, count=1)[0].entities["urls"][0]["expanded_url"]) == 0:
			reddit.subreddit("EyIran").submit(title=tweet3.text)
		elif len(API.user_timeline(screen_name=acc3, count=1)[0].entities["urls"][0]["expanded_url"]) != 0:
			reddit.subreddit("EyIran").submit(title=tweet3.text, url=API.user_timeline(screen_name=acc3, count=1)[0].entities["urls"][0]["expanded_url"])
        # Reset Loop
		latestTweet3 = tweet3

	return latestTweet3

def eventSource4(latestTweet4, tweet4):
	if latestTweet4 != tweet4:
    	# Trigger Reddit Post
		print(acc4)
		if len(API.user_timeline(screen_name=acc4, count=1)[0].entities["urls"][0]["expanded_url"]) == 0:
			reddit.subreddit("EyIran").submit(title=tweet4.text)
		elif len(API.user_timeline(screen_name=acc4, count=1)[0].entities["urls"][0]["expanded_url"]) != 0:
			reddit.subreddit("EyIran").submit(title=tweet4.text, url=API.user_timeline(screen_name=acc4, count=1)[0].entities["urls"][0]["expanded_url"])
        # Reset Loop
		latestTweet4 = tweet4

	return latestTweet4

def eventSource5(latestTweet5, tweet5):
	if latestTweet5 != tweet5:
    	# Trigger Reddit Post
		print(acc5)
		if len(API.user_timeline(screen_name=acc5, count=1)[0].entities["urls"][0]["expanded_url"]) == 0:
			reddit.subreddit("EyIran").submit(title=tweet5.text)
		elif len(API.user_timeline(screen_name=acc5, count=1)[0].entities["urls"][0]["expanded_url"]) != 0:
			reddit.subreddit("EyIran").submit(title=tweet5.text, url=API.user_timeline(screen_name=acc5, count=1)[0].entities["urls"][0]["expanded_url"])
        # Reset Loop
		latestTweet5 = tweet5

	return latestTweet5

def eventSource6(latestTweet6, tweet6):
	if latestTweet6 != tweet6:
    	# Trigger Reddit Post
		print(acc6)
		if len(API.user_timeline(screen_name=acc6, count=1)[0].entities["urls"][0]["expanded_url"]) == 0:
			reddit.subreddit("EyIran").submit(title=tweet6.text)
		elif len(API.user_timeline(screen_name=acc6, count=1)[0].entities["urls"][0]["expanded_url"]) != 0:
			reddit.subreddit("EyIran").submit(title=tweet6.text, url=API.user_timeline(screen_name=acc6, count=1)[0].entities["urls"][0]["expanded_url"])
        # Reset Loop
		latestTweet6 = tweet6

	return latestTweet6

def eventSource7(latestTweet7, tweet7):
	if latestTweet7 != tweet7:
    	# Trigger Reddit Post
		print(acc7)
		if len(API.user_timeline(screen_name=acc7, count=1)[0].entities["urls"][0]["expanded_url"]) == 0:
			reddit.subreddit("EyIran").submit(title=tweet7.text)
		elif len(API.user_timeline(screen_name=acc7, count=1)[0].entities["urls"][0]["expanded_url"]) != 0:
			reddit.subreddit("EyIran").submit(title=tweet7.text, url=API.user_timeline(screen_name=acc7, count=1)[0].entities["urls"][0]["expanded_url"])
        # Reset Loop
		latestTweet7 = tweet7

	return latestTweet7

def eventSource8(latestTweet8, tweet8):
	if latestTweet8 != tweet8:
    	# Trigger Reddit Post
		print(acc8)
		if len(API.user_timeline(screen_name=acc8, count=1)[0].entities["urls"][0]["expanded_url"]) == 0:
			reddit.subreddit("EyIran").submit(title=tweet8.text)
		elif len(API.user_timeline(screen_name=acc8, count=1)[0].entities["urls"][0]["expanded_url"]) != 0:
			reddit.subreddit("EyIran").submit(title=tweet8.text, url=API.user_timeline(screen_name=acc8, count=1)[0].entities["urls"][0]["expanded_url"])
        # Reset Loop
		latestTweet8 = tweet8

	return latestTweet8


# Replace one of the following 8 twitter accounts to change posts

acc1 = "1500tasvir"
acc2 = "AlinejadMasih"
acc3 = "IranIntl_En"
acc4 = "ICHRI"
acc5 = "NazaninBoniadi"
acc6 = "from____iran"
acc7 = "AshkanFadaei"
acc8 = "Golshifteh"

# Event Loop
def eventLoop(latestTweet1, latestTweet2, latestTweet3, latestTweet4, latestTweet5, latestTweet6, latestTweet7, latestTweet8, tweet1, tweet2, tweet3, tweet4, tweet5, tweet6, tweet7, tweet8):
	while True:
	    tweet1 = API.user_timeline(screen_name=acc1, count=1)[0]
	    tweet2 = API.user_timeline(screen_name=acc2, count=1)[0]
	    tweet3 = API.user_timeline(screen_name=acc3, count=1)[0]
	    tweet4 = API.user_timeline(screen_name=acc4, count=1)[0]
	    tweet5 = API.user_timeline(screen_name=acc5, count=1)[0]
	    tweet6 = API.user_timeline(screen_name=acc6, count=1)[0]
	    tweet7 = API.user_timeline(screen_name=acc7, count=1)[0]
	    tweet8 = API.user_timeline(screen_name=acc8, count=1)[0]
	    
	    latestTweet1 = eventSource1(latestTweet1, tweet1)
	    print("Checked: " + acc1)
	    
	    sleep(10)
	    
	    latestTweet2 = eventSource2(latestTweet2, tweet2)
	    print("Checked: " + acc2)	
		
	    sleep(10)
	    
	    latestTweet3 = eventSource3(latestTweet3, tweet3)
	    print("Checked: " + acc3)
	    
	    sleep(10)
	    
	    latestTweet4 = eventSource4(latestTweet4, tweet4)
	    print("Checked: " + acc4)
	    
	    sleep(10)
	    
	    latestTweet5 = eventSource5(latestTweet5, tweet5)
	    print("Checked: " + acc5)
	    
	    sleep(10)
	    
	    latestTweet6 = eventSource6(latestTweet6, tweet6)
	    print("Checked: " + acc6)
	    
	    sleep(10)
	    
	    latestTweet7 = eventSource7(latestTweet7, tweet7)
	    print("Checked: " + acc7)
	    
	    sleep(10)
	    
	    latestTweet8 = eventSource8(latestTweet8, tweet8)
	    print("Checked: " + acc8)
	    
	    sleep(10)
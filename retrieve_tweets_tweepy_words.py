import tweepy

# Replace these with your own API keys and access tokens as shown in the screen shot
consumer_key = 'MY_CONSUMER_KEY'
consumer_secret = 'MY_CONSUMER_SECRET'
access_token = 'MY_ACCESS_TOKEN'
access_token_secret = 'MY__ACCESS_TOKEN_SECRET'

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Set the search string
search_string = 'ELON MUSK'

# Set the number of tweets to download, we can set it to 1000
tweet_count = 100

# Search for tweets
tweets = tweepy.Cursor(api.search_tweets, q=search_string, tweet_mode='extended').items(tweet_count)

# Iterate through the tweets and print the full text
for tweet in tweets:
    print(tweet.full_text)
from dotenv import load_dotenv
import os
import twitter

load_dotenv(dotenv_path='./.env', verbose=False)

twitter_consumer_key = os.getenv('twitter_consumer_key')
twitter_consumer_secret = os.getenv('twitter_consumer_secret')
twitter_access_token = os.getenv('twitter_access_token')
twitter_access_secret = os.getenv('twitter_access_secret')



twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret,
                          access_token_key=twitter_access_token,
                          access_token_secret=twitter_access_secret)

query = "#stopasianhate"
statuses = twitter_api.GetSearch(term=query, count=100)
for status in statuses:
    print(status.text)
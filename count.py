from twython import Twython
import time

consumer_key = 'QUzB0BFumKH9wZmFHu8tBK3fW'
consumer_secret = 'QdfAIkTyc0bNqfojyNfvL62ZyZCVXan9izbqj6Wwb1VUz5YIj2'
access_token = '45138129-nsCd5XkBVvoaZAyVzphAB3xx76wBdLBXsaUCjtoKc'
access_token_secret = 'J4FPgIuzcMmHl5ah4fGJJ1XzOECxeVVxUKkemWW44Ok10'

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
lis = [535733418265681920] ## this is the latest starting tweet id
for i in range(0, 16): ## iterate through all tweets
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name="brokeymcpoverty",
    count=200, include_retweets=False, max_id=lis[-1])
    time.sleep(300) ## 5 minute rest between api calls

    for tweet in user_timeline:
        print tweet['text'] ## print the tweet
        lis.append(tweet['id']) ## append tweet id's
import tweepy
 
# Consumer keys and access tokens, used for OAuth
consumer_key = 'wnIxqoIumZQGvoGQdUgISKwM5'
consumer_secret = '9MQWQVHZ1vt2YMmmftLFe3CBmpc54J14fbMW7jz0lunAqtl9ve'
access_token = 'annapcanlas'
access_token_secret = 'xxxooo'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
# Sample method, used to update a status
api.update_status('Hello Python Central!')
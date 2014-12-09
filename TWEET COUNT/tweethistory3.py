from twython import Twython # pip install twython
import time # standard lib

''' Go to https://apps.twitter.com/ to register your app to get your api keys '''
CONSUMER_KEY = 'QUzB0BFumKH9wZmFHu8tBK3fW'
CONSUMER_SECRET = 'QdfAIkTyc0bNqfojyNfvL62ZyZCVXan9izbqj6Wwb1VUz5YIj2'
ACCESS_KEY = '45138129-nsCd5XkBVvoaZAyVzphAB3xx76wBdLBXsaUCjtoKc'
ACCESS_SECRET = 'J4FPgIuzcMmHl5ah4fGJJ1XzOECxeVVxUKkemWW44Ok10'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

lis = [533113628489449472] ## this is the latest starting tweet id 25NOV2014 1:01 PM
since = [424380485708832768] ## this is the earliest tweet id 25NOV2014 10:15 AM

import csv
with open('tweets4.csv', 'w') as fp:
    
    a = csv.writer(fp, delimiter=',')
    a.writerow(["ID","Created At","Text"])

    for i in range(0, 16): ## iterate through all tweets
    ## tweet extract method with the last list item as the max_id
        user_timeline = twitter.get_user_timeline(screen_name="byjoelanderson",since_id=since,count=200,include_retweets=False, max_id=lis[-1])
        time.sleep(300) ## 5 minute rest between api calls

        for tweet in user_timeline:
            lis.append(tweet['id']) ## append tweet id's
            a.writerow([tweet['id'],tweet['created_at'],tweet['text'].encode("utf-8")])


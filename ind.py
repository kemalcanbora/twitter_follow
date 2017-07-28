import tweepy, time, sys
import pandas as pd

# enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'E49kaUsSRgVHriNohB2Hjg'  # keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'whwJ2ylz66AEAX57h1KEUWCM2FxuHd16G0K2I0x9zPg'  # keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '144255297-7cpgMRQA53Yl0CQqnlXpTht4TKzk9jndRznpqe4B'  # keep the quotes, replace this with your access token
ACCESS_SECRET = '5L37C0B7xzOmSFI4PjqYm40BLvC0xpQuOXt1loMRdbSB3'  # keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def search_ma(user_name):
    ids = []
    for page in tweepy.Cursor(api.friends_ids, screen_name=str(user_name)).pages(): #followers_ids
        ids.extend(page)
        time.sleep(60)
        say1=(len(ids))
    return ids,len(ids)

def user_id_to_user_name(id):
    user_id_to_user_name=api.get_user(id)
    time.sleep(60)
    return user_id_to_user_name.screen_name




idsx=search_ma("kemalcanbora")

for i,item in enumerate(idsx[0]):
    try:
         decryt=user_id_to_user_name(idsx[0][i])
         d_count=search_ma(decryt)
         if d_count[1] < 600:
            # print(decryt) #name
            # print(d_count[1]) #count
            # print(d_count[0]) #id
            df=pd.DataFrame({"username":decryt,
                          "username_follow_count":d_count[1],
                          "username_follow_list":d_count[0]
            })
    except tweepy.TweepError:
        # time.sleep(60 * 15)
        continue

         # if d_count>600:
         #     pass
         # else:
         #    print(d_count[1])
         #    print(decryt)

# umutcan duman = 1614489830
print(df)
df.to_csv("deneme.csv")
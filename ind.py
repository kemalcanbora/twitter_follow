import tweepy, time, sys

# enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'i98l7OTzntnkw1V18m08ZoT5i'  # keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'lRZDJXuhmlVBpod7Nk3J8oxpP7IdnQyzVo0qaOb5ucNlLHJ9H1'  # keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '144255297-cVf3YPllVUvyx0vzaGUqwJck6UWlPDUiKkBNnXrL'  # keep the quotes, replace this with your access token
ACCESS_SECRET = 'fqbMqDdqPbd77iZhAXpgHO0H9moRZspO9l0Pyz5aHw5Ev'  # keep the quotes, replace this with your access token secret
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




idsx=search_ma("enevo")

for i,item in enumerate(idsx[0]):
         decryt=user_id_to_user_name(idsx[0][i])
         d_count=search_ma(decryt)
         print(d_count[1])
         print(decryt)

# umutcan duman = 1614489830
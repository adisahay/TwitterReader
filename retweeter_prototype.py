import twitter

api = twitter.Api(consumer_key="", # Provide Consumer Key
                consumer_secret="", # Provide Consumer Secret
                access_token_key="", # Provide Access Token Key
                access_token_secret="") # Provide Access Token Secret

tweet_id = 1032804122330845184

users = api.GetRetweeters(tweet_id)

locations = []
for user in list(users):
    user_info = api.GetUser(user)
    locations.append(user_info.location) 

print(locations)

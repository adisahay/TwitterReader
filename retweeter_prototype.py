import twitter, csv, unicodedata

api = twitter.Api(consumer_key="", # Provide Consumer Key
                consumer_secret="", # Provide Consumer Secret
                access_token_key="", # Provide Access Token Key
                access_token_secret="") # Provide Access Token Secret

tweetId = 1032804122330845184 # Replace the tweet ID value with the actual one

csvfile = open("locations.csv", "wb")
writer = csv.writer(csvfile)
writer.writerow(["Locations"]) # Set the header row

retweeters = api.GetRetweeters(tweetId) # Fetch the retweeters for this tweet

for user in list(retweeters):
    user_info = api.GetUser(user)
    # Filter out those which do not have locations
    if user_info.location != "":
        asciiString = unicodedata.normalize('NFKD', user_info.location).encode('ascii','ignore')
        writer.writerow([asciiString])

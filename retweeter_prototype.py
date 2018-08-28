import twitter, csv, unicodedata

filename = "locations.csv"

# Twitter developer credentials
consumer_key="", # Provide Consumer Key
consumer_secret="", # Provide Consumer Secret
access_token_key="", # Provide Access Token Key
access_token_secret="" # Provide Access Token Secret

api = twitter.Api(consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=access_token_key,
                access_token_secret=access_token_secret)

tweetId = 1032804122330845184 # Replace the tweet ID value with the actual one

csvfile = open(filename, "wb")
writer = csv.writer(csvfile)
writer.writerow(["Locations"]) # Set the header row

print ("Fetching retweeters for Tweet ID: " + str(tweetId))
retweeters = api.GetRetweeters(tweetId) # Fetch the retweeters for this tweet

print ("Getting retweeters location to CSV file: " + filename)
for user in list(retweeters):
    user_info = api.GetUser(user)
    # Filter out empty location values
    if user_info.location != "":
        normalized = unicodedata.normalize('NFKD', user_info.location)
        asciiString = normalized.encode('ascii','ignore')
        writer.writerow([asciiString])

print ("Finished writing to CSV file.")

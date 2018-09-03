import twitter, csv

filename = "locations.csv"

# Twitter developer credentials
consumer_key = "",
consumer_secret = "",
access_token_key = "",
access_token_secret = ""

with open("input_twitter_api_credentials.csv") as credfile:
    credentials = csv.reader(credfile, delimiter=",")
    rownum = 0
    for row in credentials:
        if rownum == 1:
            consumer_key = row[0],
            consumer_secret = row[1],
            access_token_key = row[2],
            access_token_secret = row[3]
        rownum += 1

api = twitter.Api(consumer_key="".join(consumer_key),
                consumer_secret="".join(consumer_secret),
                access_token_key="".join(access_token_key),
                access_token_secret="".join(access_token_secret))

# TODO Fetch a list of tweet ids and run the 'getRetweeters' for each of them
tweetId = 1032804122330845184 # Replace the tweet ID value with the actual one

with open(filename, "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Tweet IDs", "Retweeter Handles", "Locations"]) # Set the header row

    print ("Fetching retweeters for Tweet ID: " + str(tweetId))
    retweeters = api.GetRetweeters(tweetId) # Fetch the retweeters for this tweet

    print ("Getting retweeters location to CSV file: " + filename)
    count = 1
    found = 0
    for user in list(retweeters):
        user_info = api.GetUser(user)
        # Filter out empty location values
        if user_info.location != "":
            writer.writerow([tweetId, user_info.screen_name, user_info.location])
            found += 1
        print("\r" + str(count * 100 // len(retweeters)) + "% Completed", end="", flush=True)
        count += 1

print ("\nFinished writing to CSV file.")
print ("Total number of retweeters: " + str(len(retweeters)))
print ("Total number of locations found: " + str(found))

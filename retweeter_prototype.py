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
tweetIdList = [1032804122330845184, 1036461028429651968, 1036459095883227139]
statuses = api.GetStatuses(tweetIdList, include_entities=False, map=True)

with open(filename, "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Handles", "Tweet IDs", "Retweeter Handles", "Locations"]) # Set the header row
    found = 0
    totalCount = 0
    for tweetId in tweetIdList:
        print ("Fetching retweeters for Tweet ID: " + str(tweetId))
        retweeters = api.GetRetweeters(tweetId) # Fetch the retweeters for this tweet

        print ("Getting retweeters location to CSV file: " + filename)
        count = 1
        for user in list(retweeters):
            user_info = api.GetUser(user)
            # Filter out empty location values
            if user_info.location != "":
                writer.writerow([statuses[tweetId].AsDict()["user"]["screen_name"], tweetId, user_info.screen_name, user_info.location])
                found += 1
            print("\r" + str(count * 100 // len(retweeters)) + "% Completed", end="", flush=True)
            count += 1
        totalCount += (len(retweeters))
        print ()

print ("\nFinished writing to CSV file.")
print ("Total number of retweeters: " + str(totalCount))
print ("Total number of locations found: " + str(found))
